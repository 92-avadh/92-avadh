import os

def generate_ascii_svg():
    width = 370
    height = 280
    
    # Clean terminal ASCII banner art
    ascii_lines = [
        "   _  ___              ___                  |",
        "  / _||__ \\   ____    / _ \\ _   ____ _  __| |",
        " | (_) / /   / _  |  / /_\\ \\ \\ / / _` |/ _` |",
        "  \\__, / /_ | (_| | / / _ \\ \\ V / (_| | (_| |",
        "    /_/____| \\__,_|/_/   \\_\\ \\_/ \\__,_|\\__,_|",
        "---------------------------------------------",
        " > STATUS  : ACTIVE DEVELOPER",
        " > CODE    : CONSTANT IMPROVEMENT",
        " > MISSION : BUILD USEFUL SOFTWARE",
        " > SYSTEM  : ONLINE & READY",
        "---------------------------------------------",
        " [ ################################### ] 100%"
    ]

    lines_xml = []
    start_y = 65
    line_height = 17

    for idx, line_text in enumerate(ascii_lines):
        y = start_y + (idx * line_height)
        delay = round(0.05 + (idx * 0.06), 2)
        lines_xml.append(f'''    <g class="ascii-row" style="animation-delay: {delay}s;">
      <text x="20" y="{y}" class="art">{line_text}</text>
    </g>''')

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .bg {{ fill: #0d1117; rx: 8px; stroke: #30363d; stroke-width: 1px; }}
    .title-bar {{ fill: #161b22; rx: 8px; }}
    .title-text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 13px; font-weight: bold; fill: #3fb950; }}
    .art {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; fill: #8b949e; white-space: pre; }}
    .ascii-row {{
      opacity: 0;
      animation: typeRow 0.3s ease-out forwards;
    }}
    @keyframes typeRow {{
      0% {{ opacity: 0; transform: translateY(2px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}
  </style>

  <!-- Container -->
  <rect class="bg" width="{width}" height="{height}" />

  <!-- Window Header -->
  <rect class="title-bar" width="{width}" height="36" />
  <circle cx="20" cy="18" r="5" fill="#ff5f56" />
  <circle cx="36" cy="18" r="5" fill="#ffbd2e" />
  <circle cx="52" cy="18" r="5" fill="#27c93f" />
  <text x="72" y="22" class="title-text">terminal --avatar</text>

  <!-- ASCII Content -->
{chr(10).join(lines_xml)}
</svg>'''

    with open("avadh-ascii.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Successfully generated avadh-ascii.svg")

if __name__ == "__main__":
    generate_ascii_svg()
