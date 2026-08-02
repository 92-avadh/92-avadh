import json
import os

def render_heatmap():
    if not os.path.exists("data/contributions.json"):
        print("data/contributions.json not found. Run fetch_contributions.py first.")
        return

    with open("data/contributions.json") as f:
        data = json.load(f)

    days = data.get("days", [])
    total_contributions = data.get("total_contributions", 0)
    current_streak = data.get("current_streak", 0)
    longest_streak = data.get("longest_streak", 0)
    username = data.get("username", "92-avadh")

    # Cyberpunk / Neon Green-Cyan Palette
    PALETTE = ["#121624", "#004d40", "#00897b", "#00e676", "#00e5ff", "#76ff03"]

    width = 910
    height = 175
    box_size = 11
    gap = 4
    start_x = 42
    start_y = 52

    rects_xml = []
    
    for idx, day in enumerate(days):
        week = idx // 7
        dow = idx % 7
        if week >= 53:
            break
            
        x = start_x + week * (box_size + gap)
        y = start_y + dow * (box_size + gap)
        
        level = min(max(day.get("level", 0), 0), 5)
        color = PALETTE[level]
        
        delay = round((week * 0.012) + (dow * 0.015), 3)
        pulse_class = " pulse" if level >= 4 else ""
        
        rects_xml.append(
            f'    <rect class="box{pulse_class}" x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" ry="2" fill="{color}" style="animation-delay: {delay}s;" />'
        )

    day_labels = [
        ('<text x="22" y="79" class="lbl">Mon</text>'),
        ('<text x="22" y="110" class="lbl">Wed</text>'),
        ('<text x="22" y="141" class="lbl">Fri</text>')
    ]

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="bg-grad-heat" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080911" />
      <stop offset="50%" stop-color="#0f1322" />
      <stop offset="100%" stop-color="#05060b" />
    </linearGradient>
    <linearGradient id="border-grad-heat" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00e5ff" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#76ff03" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#7f00ff" stop-opacity="0.6" />
    </linearGradient>
    <linearGradient id="laser-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="transparent" />
      <stop offset="50%" stop-color="#00e5ff" stop-opacity="0.5" />
      <stop offset="100%" stop-color="transparent" />
    </linearGradient>
    <filter id="neon-glow-heat" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .card-bg {{ fill: url(#bg-grad-heat); rx: 12px; }}
    .card-border {{ fill: none; stroke: url(#border-grad-heat); stroke-width: 1.5px; rx: 12px; }}
    .title {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 13px; font-weight: bold; fill: #00e5ff; filter: url(#neon-glow-heat); }}
    .stats {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; fill: #8b949e; }}
    .stat-val {{ fill: #76ff03; font-weight: bold; filter: url(#neon-glow-heat); }}
    .lbl {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 9px; fill: #6e7681; }}
    .legend-text {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 10px; fill: #8b949e; }}
    
    .box {{
      opacity: 0;
      transform-origin: center;
      animation: popIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    .pulse {{
      animation: popIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards, neonPulse 2s ease-in-out infinite alternate;
    }}

    .laser-beam {{
      animation: sweepLaser 5s ease-in-out infinite;
    }}

    @keyframes popIn {{
      0% {{ opacity: 0; transform: translateY(6px) scale(0.7); }}
      100% {{ opacity: 1; transform: translateY(0) scale(1); }}
    }}

    @keyframes neonPulse {{
      0% {{ opacity: 0.8; filter: drop-shadow(0 0 1px #76ff03); }}
      100% {{ opacity: 1; filter: drop-shadow(0 0 4px #76ff03); }}
    }}

    @keyframes sweepLaser {{
      0% {{ transform: translateX(0); opacity: 0; }}
      15% {{ opacity: 1; }}
      85% {{ opacity: 1; }}
      100% {{ transform: translateX(820px); opacity: 0; }}
    }}
  </style>

  <!-- Background -->
  <rect class="card-bg" width="{width}" height="{height}" />
  <rect class="card-border" width="{width}" height="{height}" />

  <!-- Header -->
  <text x="22" y="28" class="title">⚡ {username} / live-contribution-heatmap</text>
  <text x="590" y="28" class="stats">
    Total: <tspan class="stat-val">{total_contributions:,}</tspan> | 
    Streak: <tspan class="stat-val">{current_streak}d</tspan> | 
    Best: <tspan class="stat-val">{longest_streak}d</tspan>
  </text>

  <line x1="0" y1="38" width="{width}" x2="{width}" y2="38" stroke="#21263d" stroke-width="1" />

  <!-- Day Labels -->
  {''.join(day_labels)}

  <!-- Grid -->
  <g>
{chr(10).join(rects_xml)}
  </g>

  <!-- Laser Radar Beam -->
  <g class="laser-beam">
    <rect x="42" y="48" width="40" height="110" fill="url(#laser-grad)" />
  </g>

  <!-- Legend -->
  <g transform="translate(745, 155)">
    <text x="-32" y="9" class="legend-text">Less</text>
    <rect x="0" y="0" width="10" height="10" rx="2" fill="#121624" />
    <rect x="13" y="0" width="10" height="10" rx="2" fill="#004d40" />
    <rect x="26" y="0" width="10" height="10" rx="2" fill="#00897b" />
    <rect x="39" y="0" width="10" height="10" rx="2" fill="#00e676" />
    <rect x="52" y="0" width="10" height="10" rx="2" fill="#00e5ff" />
    <rect x="65" y="0" width="10" height="10" rx="2" fill="#76ff03" />
    <text x="80" y="9" class="legend-text">More</text>
  </g>
</svg>'''

    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Successfully generated ultra-animated contrib-heatmap.svg")

if __name__ == "__main__":
    render_heatmap()
