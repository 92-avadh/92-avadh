import os

def render_info_card():
    width = 490
    height = 280
    username = "92-avadh"

    lines = [
        ("OS", "GitHub / Cloud Architecture"),
        ("Host", "Developer Workstation"),
        ("Kernel", "Full Stack & System Design"),
        ("Uptime", "24/7 Continuous Learning"),
        ("Stack", "TypeScript, React, Python, Node.js"),
        ("Tools", "Git, Docker, VS Code, CI/CD Actions"),
        ("Focus", "Building high-performance software & AI tooling"),
        ("Status", "🟢 Open for collaboration & open-source")
    ]

    lines_xml = []
    start_y = 70
    line_height = 24

    for idx, (label, val) in enumerate(lines):
        y = start_y + (idx * line_height)
        delay = round(0.1 + (idx * 0.08), 2)
        
        lines_xml.append(f'''    <g class="line" style="animation-delay: {delay}s;">
      <text x="25" y="{y}" class="label">{label}:</text>
      <text x="110" y="{y}" class="value">{val}</text>
    </g>''')

    # Color palette squares at bottom
    colors = ["#ff5f56", "#ffbd2e", "#27c93f", "#58a6ff", "#bc8cff", "#39d353"]
    color_squares = []
    for idx, c in enumerate(colors):
        x = 25 + (idx * 22)
        color_squares.append(f'<rect x="{x}" y="245" width="16" height="16" rx="3" fill="{c}" />')

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .card-bg {{ fill: #0d1117; rx: 8px; stroke: #30363d; stroke-width: 1px; }}
    .title-bar {{ fill: #161b22; rx: 8px; }}
    .dot {{ rx: 50%; }}
    .title-text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 13px; font-weight: bold; fill: #e6edf3; }}
    .label {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12px; font-weight: bold; fill: #58a6ff; }}
    .value {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12px; fill: #c9d1d9; }}
    .line {{
      opacity: 0;
      animation: fadeInLine 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}
    @keyframes fadeInLine {{
      0% {{ opacity: 0; transform: translateX(-8px); }}
      100% {{ opacity: 1; transform: translateX(0); }}
    }}
  </style>

  <!-- Background -->
  <rect class="card-bg" width="{width}" height="{height}" />

  <!-- Title Bar Window Controls -->
  <rect class="title-bar" width="{width}" height="36" />
  <circle cx="20" cy="18" r="5" fill="#ff5f56" />
  <circle cx="36" cy="18" r="5" fill="#ffbd2e" />
  <circle cx="52" cy="18" r="5" fill="#27c93f" />
  <text x="72" y="22" class="title-text">neofetch --user {username}</text>

  <!-- Info Lines -->
{chr(10).join(lines_xml)}

  <!-- Terminal Color Palette Footer -->
  <g class="line" style="animation-delay: 0.8s;">
    {''.join(color_squares)}
  </g>
</svg>'''

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Successfully generated info-card.svg")

if __name__ == "__main__":
    render_info_card()
