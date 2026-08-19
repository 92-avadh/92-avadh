import os

def generate_ascii_svg():
    width = 370
    height = 280
    username = "andriidrok1"

    ascii_art_lines = [
        r"   _   _  _ ___  ___  ____ ___  ___  ___  _  __",
        r"  /_\ | \| |   \| _ \|_  _|_ _| |   \/ _ \| |/ /",
        r" / _ \| .` | |) |   /  _|  | |  | |) | (_) | ' < ",
        r"/_/ \_\_|\_|___/|_|_\___|___| |___/\___/|_|\_\\",
        r" --------------------------------------------",
        r"  ROLE    : CS Student @ SFSU (SF Bay Area)",
        r"  FOCUS   : Full Stack Dev & AI Tools",
        r"  STACK   : Python, TS, React, FastAPI, Docker",
        r"  STATUS  : 🟢 Active & Open Source Dev",
        r" --------------------------------------------",
        r" [####################################] 100%"
    ]

    rows_xml = []
    start_y = 65
    line_height = 17

    for idx, line in enumerate(ascii_art_lines):
        y = start_y + (idx * line_height)
        delay = round(0.05 + (idx * 0.06), 2)
        
        if "andriidrok1" in line or "ROLE" in line:
            color = "#00f2fe"
        elif "STATUS" in line or "100%" in line:
            color = "#50fa7b"
        elif "----" in line:
            color = "#444c56"
        else:
            color = "#8b949e"

        safe_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        rows_xml.append(f'''    <g class="row" style="animation-delay: {delay}s;">
      <text x="20" y="{y}" fill="{color}" class="code">{safe_line}</text>
    </g>''')

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; }}
    .title-bar {{ fill: #161b22; }}
    .title-text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12px; font-weight: bold; fill: #3fb950; }}
    .code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; white-space: pre; }}
    
    .row {{
      opacity: 0;
      animation: typeIn 0.3s ease-out forwards;
    }}
    
    .cursor {{
      animation: blink 0.9s infinite;
      fill: #50fa7b;
    }}

    @keyframes typeIn {{
      0% {{ opacity: 0; transform: translateY(3px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes blink {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
    }}
  </style>

  <!-- Card Background -->
  <rect class="bg" width="{width}" height="{height}" rx="8" ry="8" />

  <!-- Window Controls Header -->
  <rect class="title-bar" width="{width}" height="36" rx="8" ry="8" />
  <circle cx="20" cy="18" r="5" fill="#ff5f56" />
  <circle cx="36" cy="18" r="5" fill="#ffbd2e" />
  <circle cx="52" cy="18" r="5" fill="#27c93f" />
  <text x="72" y="22" class="title-text">terminal --avatar {username}</text>

  <!-- ASCII Art Content -->
{chr(10).join(rows_xml)}

  <!-- Blinking Cursor -->
  <rect class="cursor" x="338" y="235" width="8" height="12" rx="1" ry="1" />
</svg>'''

    with open("andriidrok1-ascii.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Successfully updated andriidrok1-ascii.svg")

if __name__ == "__main__":
    generate_ascii_svg()
