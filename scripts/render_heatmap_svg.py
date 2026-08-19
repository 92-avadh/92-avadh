import json
import os

def render_heatmap():
    if not os.path.exists("data/contributions.json"):
        print("data/contributions.json not found. Run fetch_contributions.py first.")
        return

    with open("data/contributions.json", encoding="utf-8") as f:
        data = json.load(f)

    days = data.get("days", [])
    total_contributions = data.get("total_contributions", 0)
    current_streak = data.get("current_streak", 0)
    longest_streak = data.get("longest_streak", 0)
    username = data.get("username", "andriidrok1")

    PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

    width = 860
    height = 160
    box_size = 11
    gap = 4
    start_x = 35
    start_y = 45

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
        
        rects_xml.append(
            f'    <rect class="box" x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" ry="2" fill="{color}" style="animation-delay: {delay}s;" />'
        )

    day_labels = [
        ('<text x="18" y="72" class="lbl">Mon</text>'),
        ('<text x="18" y="102" class="lbl">Wed</text>'),
        ('<text x="18" y="132" class="lbl">Fri</text>')
    ]

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; }}
    .title {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 13px; font-weight: bold; fill: #58a6ff; }}
    .stats {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; fill: #8b949e; }}
    .stat-val {{ fill: #3fb950; font-weight: bold; }}
    .lbl {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 9px; fill: #6e7681; }}
    .legend-text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 10px; fill: #8b949e; }}
    
    .box {{
      opacity: 0;
      animation: popIn 0.35s ease-out forwards;
    }}

    @keyframes popIn {{
      0% {{ opacity: 0; transform: translateY(5px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}
  </style>

  <!-- Background -->
  <rect class="bg" width="{width}" height="{height}" rx="8" ry="8" />

  <!-- Header & Stats -->
  <text x="20" y="26" class="title">⚡ {username} / contribution-graph</text>
  <text x="560" y="26" class="stats">
    Total: <tspan class="stat-val">{total_contributions:,}</tspan> | 
    Streak: <tspan class="stat-val">{current_streak}d</tspan> | 
    Best: <tspan class="stat-val">{longest_streak}d</tspan>
  </text>

  <!-- Day Labels -->
  {''.join(day_labels)}

  <!-- Grid -->
  <g>
{chr(10).join(rects_xml)}
  </g>

  <!-- Legend -->
  <g transform="translate(710, 137)">
    <text x="-32" y="9" class="legend-text">Less</text>
    <rect x="0" y="0" width="10" height="10" rx="2" ry="2" fill="#161b22" />
    <rect x="13" y="0" width="10" height="10" rx="2" fill="#0e4429" />
    <rect x="26" y="0" width="10" height="10" rx="2" fill="#006d32" />
    <rect x="39" y="0" width="10" height="10" rx="2" fill="#26a641" />
    <rect x="52" y="0" width="10" height="10" rx="2" fill="#39d353" />
    <rect x="65" y="0" width="10" height="10" rx="2" fill="#69f0a0" />
    <text x="80" y="9" class="legend-text">More</text>
  </g>
</svg>'''

    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Successfully updated contrib-heatmap.svg")

if __name__ == "__main__":
    render_heatmap()
