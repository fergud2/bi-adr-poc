#!/usr/bin/env python3

from __future__ import annotations

import argparse
import pathlib
import markdown


HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <style>
    body {{
      font-family: Arial, sans-serif;
      line-height: 1.5;
      margin: 0;
      background: #f6f8fa;
      color: #24292f;
    }}

    header {{
      background: #0f172a;
      color: white;
      padding: 24px 40px;
    }}

    main {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 32px;
      background: white;
    }}

    h1, h2, h3 {{
      color: #0f172a;
    }}

    table {{
      border-collapse: collapse;
      width: 100%;
      margin: 16px 0 32px 0;
      font-size: 14px;
    }}

    th, td {{
      border: 1px solid #d0d7de;
      padding: 8px 10px;
      text-align: left;
      vertical-align: top;
    }}

    th {{
      background: #f3f4f6;
      font-weight: 700;
    }}

    tr:nth-child(even) {{
      background: #fafafa;
    }}

    code {{
      background: #eef2f7;
      padding: 2px 5px;
      border-radius: 4px;
    }}

    a {{
      color: #0969da;
    }}

    .container {{
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
      min-height: 100vh;
    }}

    @media print {{
      body {{
        background: white;
      }}

      header {{
        background: white;
        color: black;
        border-bottom: 1px solid #ccc;
      }}

      main {{
        box-shadow: none;
        padding: 16px;
      }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>{title}</h1>
    <p>Generated ADR governance report</p>
  </header>

  <main class="container">
    {body}
  </main>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert ADR Markdown report to standalone HTML.")
    parser.add_argument("--input", required=True, help="Input Markdown report path.")
    parser.add_argument("--output", required=True, help="Output HTML report path.")
    parser.add_argument("--title", default="ADR Report", help="HTML page title.")
    args = parser.parse_args()

    input_path = pathlib.Path(args.input)
    output_path = pathlib.Path(args.output)

    markdown_text = input_path.read_text(encoding="utf-8")

    body = markdown.markdown(
        markdown_text,
        extensions=[
            "tables",
            "fenced_code",
            "toc",
        ],
    )

    html = HTML_TEMPLATE.format(title=args.title, body=body)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")

    print(f"Wrote HTML report to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())