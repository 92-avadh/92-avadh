import os

def render_info_card():
    width = 490
    height = 300
    username = "92-avadh"

    skills = [
        ("TypeScript / JS", 95, "#00f2fe"),
        ("Python & Scripting", 90, "#ff79c6"),
        ("React / Next.js", 92, "#50fa7b"),
        ("Node.js / APIs", 88, "#ffb86c"),
        ("Cloud & CI/CD", 85, "#bd93f9")
    ]

    details = [
        ("OS", "Linux / macOS / Windows Dev Env"),
        ("Kernel", "Full-Stack Software Engineering"),
        ("Uptime", "24/7 Continuous Deployment & Learning"),
        ("Status", "🟢 Open for Innovative Projects")
    ]

    xml_elements = []
    
    # Render Details
    start_y = 65
    for idx, (label, val) in enumerate(details):
        y = start_y + (idx * 20)
        delay = round(0.1 + (idx * 0.08), 2)
        val_color = "#50fa7b" if "🟢" in val else "#f8f8f2"
        xml_elements.append(f'''    <g class="fade-item" style="animation-delay: {delay}s;">
      <text x="22" y="{y}" class="label">{label}:</text>
      <text x="95" y="{y}" class="val" fill="{val_color}">{val}</text>
    </g>''')

    # Separator Line
    xml_elements.append('''    <line x1="22" y1="152" x2="468" y2="152" stroke="#21263d" stroke-width="1" />''')
    xml_elements.append('''    <text x="22" y="170" class="section-title">⚡ TECH STACK & PROFICIENCY</text>''')

    # Render Skill Bars
    skill_start_y = 190
    for idx, (skill_name, percent, color) in enumerate(skills):
        y = skill_start_y + (idx * 20)
        delay = round(0.45 + (idx * 0.09), 2)
        bar_width = int((percent / 100) * 180)
        
        xml_elements.append(f'''    <g class="fade-item" style="animation-delay: {delay}s;">
      <text x="22" y="{y}" class="skill-name">{skill_name}</text>
      <rect x="190" y="{y-10}" width="180" height="8" rx="4" fill="#161b2e" />
      <rect x="190" y="{y-10}" width="{bar_width}" height="8" rx="4" fill="{color}" class="bar-fill" style="animation-delay: {delay+0.1}s;" />
      <text x="380" y="{y}" class="percent-text" fill="{color}">{percent}%</text>
    </g>''')

    # Terminal Palette Footer
    palette_colors = ["#ff5f56", "#ffbd2e", "#27c93f", "#00f2fe", "#bd93f9", "#ff79c6", "#50fa7b", "#f1fa8c"]
    squares = []
    for idx, c in enumerate(palette_colors):
        x = 22 + (idx * 20)
        squares.append(f'<rect x="{x}" y="273" width="14" height="14" rx="3" fill="{c}" />')

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="bg-grad-card" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080911" />
      <stop offset="50%" stop-color="#0f1322" />
      <stop offset="100%" stop-color="#05060b" />
    </linearGradient>
    <linearGradient id="header-grad-card" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#161b2e" />
      <stop offset="100%" stop-color="#0d111d" />
    </linearGradient>
    <linearGradient id="border-grad-card" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#50fa7b" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#00f2fe" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#bd93f9" stop-opacity="0.6" />
    </linearGradient>
    <filter id="neon-glow-card" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .card-bg {{ fill: url(#bg-grad-card); rx: 12px; }}
    .card-border {{ fill: none; stroke: url(#border-grad-card); stroke-width: 1.5px; rx: 12px; }}
    .title-bar {{ fill: url(#header-grad-card); rx: 12px; }}
    .title-text {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 13px; font-weight: bold; fill: #50fa7b; filter: url(#neon-glow-card); }}
    .section-title {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; font-weight: bold; fill: #00f2fe; letter-spacing: 1px; }}
    .label {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; font-weight: bold; fill: #bd93f9; }}
    .val {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; }}
    .skill-name {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; fill: #f8f8f2; }}
    .percent-text {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 10px; font-weight: bold; }}
    
    .fade-item {{
      opacity: 0;
      animation: fadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    .bar-fill {{
      transform-origin: left;
      animation: fillBar 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    @keyframes fadeIn {{
      0% {{ opacity: 0; transform: translateX(-6px); }}
      100% {{ opacity: 1; transform: translateX(0); }}
    }}

    @keyframes fillBar {{
      0% {{ transform: scaleX(0); }}
      100% {{ transform: scaleX(1); }}
    }}
  </style>

  <!-- Background Card -->
  <rect class="card-bg" width="{width}" height="{height}" />
  <rect class="card-border" width="{width}" height="{height}" />

  <!-- Window Header -->
  <rect class="title-bar" width="{width}" height="38" />
  <rect x="0" y="37" width="{width}" height="1" fill="#21263d" />
  <circle cx="20" cy="19" r="5" fill="#ff5f56" />
  <circle cx="36" cy="19" r="5" fill="#ffbd2e" />
  <circle cx="52" cy="19" r="5" fill="#27c93f" />
  <text x="72" y="23" class="title-text">neofetch --sysinfo {username}</text>

  <!-- Info Content -->
{chr(10).join(xml_elements)}

  <!-- Footer Palette -->
  <g class="fade-item" style="animation-delay: 0.9s;">
    {''.join(squares)}
  </g>
</svg>'''

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Successfully generated ultra-animated info-card.svg")

if __name__ == "__main__":
    render_info_card()
