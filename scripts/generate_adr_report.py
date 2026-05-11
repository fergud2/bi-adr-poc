#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import subprocess
import sys
from dataclasses import dataclass
from typing import Any

try:
    import yaml
except ImportError:
    print("Missing dependency: pyyaml. Install with: pip install pyyaml", file=sys.stderr)
    raise


FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

VALID_STATUSES = {
    "Proposed",
    "Accepted",
    "Rejected",
    "Superseded",
    "Deprecated",
}


@dataclass(frozen=True)
class ADR:
    id: str
    title: str
    status: str
    date: str
    owner: str
    application: str
    system: str
    domain: str
    tags: list[str]
    review_date: str | None
    supersedes: str | None
    superseded_by: str | None
    path: pathlib.Path
    last_modified_date: str | None = None
    last_modified_author: str | None = None
    last_modified_commit: str | None = None


def run_git(path: pathlib.Path, args: list[str]) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args, "--", str(path)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return result.stdout.strip() or None
    except Exception:
        return None


def git_metadata(path: pathlib.Path) -> tuple[str | None, str | None, str | None]:
    last_date = run_git(path, ["log", "-1", "--format=%ad", "--date=short"])
    last_author = run_git(path, ["log", "-1", "--format=%an"])
    last_commit = run_git(path, ["log", "-1", "--format=%h"])
    return last_date, last_author, last_commit


def parse_front_matter(path: pathlib.Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None
    return yaml.safe_load(match.group(1)) or {}


def normalize_optional(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def parse_adr(path: pathlib.Path, include_git: bool) -> ADR | None:
    metadata = parse_front_matter(path)
    if metadata is None:
        return None

    last_date = last_author = last_commit = None
    if include_git:
        last_date, last_author, last_commit = git_metadata(path)

    return ADR(
        id=str(metadata.get("id", "")).strip(),
        title=str(metadata.get("title", path.stem)).strip(),
        status=str(metadata.get("status", "Unknown")).strip(),
        date=str(metadata.get("date", "")).strip(),
        owner=str(metadata.get("owner", "Unknown")).strip(),
        application=str(metadata.get("application", "Unknown")).strip(),
        system=str(metadata.get("system", "Unknown")).strip(),
        domain=str(metadata.get("domain", "Unknown")).strip(),
        tags=[str(tag).strip() for tag in (metadata.get("tags", []) or [])],
        review_date=normalize_optional(metadata.get("review_date")),
        supersedes=normalize_optional(metadata.get("supersedes")),
        superseded_by=normalize_optional(metadata.get("superseded_by")),
        path=path,
        last_modified_date=last_date,
        last_modified_author=last_author,
        last_modified_commit=last_commit,
    )


def load_adrs(adr_dir: pathlib.Path, include_git: bool) -> list[ADR]:
    adrs: list[ADR] = []
    for path in sorted(adr_dir.glob("*.md")):
        adr = parse_adr(path, include_git=include_git)
        if adr:
            adrs.append(adr)
    return adrs


def filter_adrs(
    adrs: list[ADR],
    application: str | None,
    system: str | None,
    domain: str | None,
    tag: str | None,
) -> list[ADR]:
    filtered = adrs

    if application:
        filtered = [adr for adr in filtered if adr.application == application]

    if system:
        filtered = [adr for adr in filtered if adr.system == system]

    if domain:
        filtered = [adr for adr in filtered if adr.domain == domain]

    if tag:
        filtered = [adr for adr in filtered if tag in adr.tags]

    return filtered


def parse_iso_date(value: str | None) -> dt.date | None:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def days_overdue(review_date: str | None, today: dt.date) -> int | None:
    parsed = parse_iso_date(review_date)
    if not parsed:
        return None
    diff = (today - parsed).days
    return diff if diff > 0 else None


def markdown_table(rows: list[list[str]], headers: list[str]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        cleaned = [str(cell).replace("\n", " ").replace("|", "\\|") for cell in row]
        lines.append("| " + " | ".join(cleaned) + " |")
    return "\n".join(lines)


def group_counts(values: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items()))


def validate_adrs(adrs: list[ADR]) -> list[str]:
    errors: list[str] = []
    seen_ids: dict[str, pathlib.Path] = {}

    for adr in adrs:
        prefix = str(adr.path)

        if not adr.id:
            errors.append(f"{prefix}: missing id")

        if adr.id in seen_ids:
            errors.append(f"{prefix}: duplicate id {adr.id}; first seen at {seen_ids[adr.id]}")
        elif adr.id:
            seen_ids[adr.id] = adr.path

        if not adr.title:
            errors.append(f"{prefix}: missing title")

        if adr.status not in VALID_STATUSES:
            errors.append(f"{prefix}: invalid status '{adr.status}'")

        if not parse_iso_date(adr.date):
            errors.append(f"{prefix}: invalid or missing date '{adr.date}'")

        if not adr.owner or adr.owner == "Unknown":
            errors.append(f"{prefix}: missing owner")

        if not adr.application or adr.application == "Unknown":
            errors.append(f"{prefix}: missing application")

        if not adr.system or adr.system == "Unknown":
            errors.append(f"{prefix}: missing system")

        if adr.status == "Accepted" and not parse_iso_date(adr.review_date):
            errors.append(f"{prefix}: accepted ADR must have a valid review_date")

    return errors


def generate_report(adrs: list[ADR], title: str) -> str:
    today = dt.date.today()

    status_counts = group_counts([adr.status for adr in adrs])
    owner_counts = group_counts([adr.owner for adr in adrs])
    domain_counts = group_counts([adr.domain for adr in adrs])

    all_tags: list[str] = []
    for adr in adrs:
        all_tags.extend(adr.tags)
    tag_counts = group_counts(all_tags)

    overdue = [
        adr for adr in adrs
        if days_overdue(adr.review_date, today) is not None
        and adr.status in {"Accepted", "Proposed"}
    ]

    proposed = [adr for adr in adrs if adr.status == "Proposed"]
    superseded_or_deprecated = [
        adr for adr in adrs if adr.status in {"Superseded", "Deprecated"}
    ]

    lines: list[str] = []

    lines.append(f"# ADR Report: {title}")
    lines.append("")
    lines.append(f"Generated on: `{today.isoformat()}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total ADRs: {len(adrs)}")
    for status, count in status_counts.items():
        lines.append(f"- {status}: {count}")
    lines.append(f"- Proposed decisions: {len(proposed)}")
    lines.append(f"- Overdue reviews: {len(overdue)}")
    lines.append("")

    lines.append("## ADRs by Status")
    lines.append("")
    lines.append(markdown_table([[k, str(v)] for k, v in status_counts.items()], ["Status", "Count"]))
    lines.append("")

    lines.append("## ADRs by Domain")
    lines.append("")
    lines.append(markdown_table([[k, str(v)] for k, v in domain_counts.items()], ["Domain", "Count"]))
    lines.append("")

    lines.append("## ADRs by Owner")
    lines.append("")
    lines.append(markdown_table([[k, str(v)] for k, v in owner_counts.items()], ["Owner", "Count"]))
    lines.append("")

    lines.append("## Top Tags")
    lines.append("")
    top_tags = sorted(tag_counts.items(), key=lambda item: (-item[1], item[0]))[:20]
    lines.append(markdown_table([[k, str(v)] for k, v in top_tags], ["Tag", "Count"]))
    lines.append("")

    lines.append("## Decisions Requiring Review")
    lines.append("")
    if overdue:
        rows = [
            [
                adr.id,
                adr.title,
                adr.status,
                adr.review_date or "",
                adr.owner,
                str(days_overdue(adr.review_date, today)),
                str(adr.path),
            ]
            for adr in sorted(overdue, key=lambda a: parse_iso_date(a.review_date) or today)
        ]
        lines.append(markdown_table(rows, ["ID", "Title", "Status", "Review Date", "Owner", "Days Overdue", "File"]))
    else:
        lines.append("No ADRs are currently overdue for review.")
    lines.append("")

    lines.append("## Proposed Decisions")
    lines.append("")
    if proposed:
        rows = [
            [adr.id, adr.title, adr.date, adr.owner, ", ".join(adr.tags), str(adr.path)]
            for adr in sorted(proposed, key=lambda a: a.date)
        ]
        lines.append(markdown_table(rows, ["ID", "Title", "Date", "Owner", "Tags", "File"]))
    else:
        lines.append("No proposed ADRs.")
    lines.append("")

    lines.append("## Superseded or Deprecated Decisions")
    lines.append("")
    if superseded_or_deprecated:
        rows = [
            [
                adr.id,
                adr.title,
                adr.status,
                adr.superseded_by or "",
                adr.date,
                str(adr.path),
            ]
            for adr in sorted(superseded_or_deprecated, key=lambda a: a.id)
        ]
        lines.append(markdown_table(rows, ["ID", "Title", "Status", "Superseded By", "Date", "File"]))
    else:
        lines.append("No superseded or deprecated ADRs.")
    lines.append("")

    lines.append("## All ADRs")
    lines.append("")
    rows = [
        [
            adr.id,
            adr.title,
            adr.status,
            adr.date,
            adr.owner,
            adr.domain,
            ", ".join(adr.tags),
            adr.review_date or "",
            adr.supersedes or "",
            adr.superseded_by or "",
            str(adr.path),
        ]
        for adr in sorted(adrs, key=lambda a: a.id)
    ]
    lines.append(markdown_table(rows, ["ID", "Title", "Status", "Date", "Owner", "Domain", "Tags", "Review Date", "Supersedes", "Superseded By", "File"]))
    lines.append("")

    if any(adr.last_modified_date for adr in adrs):
        lines.append("## Git History")
        lines.append("")
        rows = [
            [
                adr.id,
                adr.title,
                adr.last_modified_date or "",
                adr.last_modified_author or "",
                adr.last_modified_commit or "",
            ]
            for adr in sorted(adrs, key=lambda a: a.last_modified_date or "", reverse=True)
        ]
        lines.append(markdown_table(rows, ["ID", "Title", "Last Modified", "Author", "Commit"]))
        lines.append("")

    lines.append("## Decision Timeline")
    lines.append("")
    rows = [
        [adr.date, adr.id, adr.title, adr.status, adr.owner]
        for adr in sorted(adrs, key=lambda a: (a.date, a.id))
    ]
    lines.append(markdown_table(rows, ["Date", "ID", "Title", "Status", "Owner"]))
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Markdown ADR report.")
    parser.add_argument("--adr-dir", default="docs/adr", help="Directory containing ADR Markdown files.")
    parser.add_argument("--application", help="Filter by application metadata.")
    parser.add_argument("--system", help="Filter by system metadata.")
    parser.add_argument("--domain", help="Filter by domain metadata.")
    parser.add_argument("--tag", help="Filter by tag.")
    parser.add_argument("--title", default="ADR Report", help="Report title.")
    parser.add_argument("--output", default="docs/reports/adr-report.md", help="Output Markdown report path.")
    parser.add_argument("--validate-only", action="store_true", help="Validate ADRs but do not generate a report.")
    parser.add_argument("--include-git", action="store_true", help="Add Git last-modified metadata when available.")
    args = parser.parse_args()

    adr_dir = pathlib.Path(args.adr_dir)
    if not adr_dir.exists():
        print(f"ADR directory not found: {adr_dir}", file=sys.stderr)
        return 2

    all_adrs = load_adrs(adr_dir, include_git=args.include_git)
    errors = validate_adrs(all_adrs)

    if errors:
        print("ADR validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    if args.validate_only:
        print(f"Validated {len(all_adrs)} ADRs successfully.")
        return 0

    filtered = filter_adrs(
        all_adrs,
        application=args.application,
        system=args.system,
        domain=args.domain,
        tag=args.tag,
    )

    report = generate_report(filtered, args.title)
    output = pathlib.Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print(f"Wrote ADR report to {output}")
    print(f"Included ADRs: {len(filtered)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
