import os

def render_info_card():
    width = 490
    height = 280
    username = "andriidrok1"

    details = [
        ("User", "Andrii Drok (andriidrok1)"),
        ("Degree", "CS @ San Francisco State University"),
        ("Stack", "Python, TypeScript, React, FastAPI, Docker"),
        ("Projects", "autobroll, strategy-checker, compound"),
        ("Uptime", "24/7 Building & Backtesting"),
        ("Focus", "AI Video Tools & Quantitative Markets"),
        ("Status", "🟢 Open for Open-Source & Collabs")
    ]

    skills = [
        ("Python / FastAPI", 94, "#58a6ff"),
        ("TypeScript / React", 90, "#3fb950"),
        ("Three.js & Docker", 85, "#bc8cff")
    ]

    xml_elements = []
    
    # Details
    start_y = 65
    for idx, (label, val) in enumerate(details):
        y = start_y + (idx * 20)
        delay = round(0.08 + (idx * 0.06), 2)
        val_color = "#3fb950" if "🟢" in val else "#c9d1d9"
        xml_elements.append(f'''    <g class="fade-item" style="animation-delay: {delay}s;">
      <text x="20" y="{y}" class="label">{label}:</text>
      <text x="95" y="{y}" class="val" fill="{val_color}">{val}</text>
    </g>''')

    # Skill Bars
    skill_start_y = 210
    for idx, (skill_name, percent, color) in enumerate(skills):
        y = skill_start_y + (idx * 18)
        delay = round(0.5 + (idx * 0.08), 2)
        bar_width = int((percent / 100) * 160)
        
        xml_elements.append(f'''    <g class="fade-item" style="animation-delay: {delay}s;">
      <text x="20" y="{y}" class="skill-name">{skill_name}</text>
      <rect x="180" y="{y-9}" width="160" height="7" rx="3" ry="3" fill="#161b22" />
      <rect x="180" y="{y-9}" width="{bar_width}" height="7" rx="3" ry="3" fill="{color}" />
      <text x="350" y="{y}" class="percent-text" fill="{color}">{percent}%</text>
    </g>''')

    # Color dots footer
    palette_colors = ["#ff5f56", "#ffbd2e", "#27c93f", "#58a6ff", "#bc8cff", "#3fb950", "#d2a8ff"]
    squares = []
    for idx, c in enumerate(palette_colors):
        x = 400 + (idx * 11)
        squares.append(f'<rect x="{x}" y="255" width="8" height="8" rx="2" ry="2" fill="{c}" />')

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .card-bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; }}
    .title-bar {{ fill: #161b22; }}
    .title-text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 13px; font-weight: bold; fill: #58a6ff; }}
    .label {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; font-weight: bold; fill: #58a6ff; }}
    .val {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; }}
    .skill-name {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 10px; fill: #8b949e; }}
    .percent-text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 10px; font-weight: bold; }}
    
    .fade-item {{
      opacity: 0;
      animation: fadeIn 0.4s ease-out forwards;
    }}

    @keyframes fadeIn {{
      0% {{ opacity: 0; transform: translateX(-5px); }}
      100% {{ opacity: 1; transform: translateX(0); }}
    }}
  </style>

  <!-- Background -->
  <rect class="card-bg" width="{width}" height="{height}" rx="8" ry="8" />

  <!-- Title Bar -->
  <rect class="title-bar" width="{width}" height="36" rx="8" ry="8" />
  <circle cx="20" cy="18" r="5" fill="#ff5f56" />
  <circle cx="36" cy="18" r="5" fill="#ffbd2e" />
  <circle cx="52" cy="18" r="5" fill="#27c93f" />
  <text x="72" y="22" class="title-text">neofetch --user {username}</text>

  <!-- Info Content -->
{chr(10).join(xml_elements)}

  <!-- Footer Palette -->
  <g class="fade-item" style="animation-delay: 0.8s;">
    {''.join(squares)}
  </g>
</svg>'''

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Successfully updated info-card.svg")

if __name__ == "__main__":
    render_info_card()
