import os

def generate_ascii_svg():
    width = 410
    height = 300
    username = "92-avadh"

    ascii_art_lines = [
        "  ___ ___         _  _  _   _  ___  ___ ",
        " / _ |_  |  __ _ | || || | / |/ _ \\/ _ \\",
        " \\_, / / / / _` || || || |_| | (_) | (_) |",
        "   /_/___| \\__,_||_||_||_/\\___/\\___/\\___/ ",
        " ----------------------------------------",
        "  SYSTEM   : CYBER-TERMINAL v3.0",
        "  USER     : 92-avadh (FULL STACK DEV)",
        "  STATUS   : 🟢 ACTIVE & COLLABORATING",
        "  LOCATION : GLOBAL / CLOUD",
        " ----------------------------------------",
        " [██████████████████████████████████] 100%"
    ]

    rows_xml = []
    start_y = 70
    line_height = 18

    for idx, line in enumerate(ascii_art_lines):
        y = start_y + (idx * line_height)
        delay = round(0.1 + (idx * 0.07), 2)
        color = "#00f2fe" if "92-avadh" in line or "100%" in line else ("#ff79c6" if "STATUS" in line else "#8be9fd")
        
        rows_xml.append(f'''    <g class="row" style="animation-delay: {delay}s;">
      <text x="22" y="{y}" fill="{color}" class="code-text">{line}</text>
    </g>''')

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <!-- Gradients -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080911" />
      <stop offset="50%" stop-color="#0f1322" />
      <stop offset="100%" stop-color="#05060b" />
    </linearGradient>
    <linearGradient id="header-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#161b2e" />
      <stop offset="100%" stop-color="#0d111d" />
    </linearGradient>
    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#7f00ff" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#ff0844" stop-opacity="0.6" />
    </linearGradient>
    
    <!-- Glow Filter -->
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .card-bg {{ fill: url(#bg-grad); rx: 12px; }}
    .card-border {{ fill: none; stroke: url(#border-grad); stroke-width: 1.5px; rx: 12px; }}
    .title-bar {{ fill: url(#header-grad); rx: 12px; }}
    .title-text {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 13px; font-weight: bold; fill: #00f2fe; filter: url(#neon-glow); }}
    .code-text {{ font-family: 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; white-space: pre; }}
    
    .row {{
      opacity: 0;
      animation: typeIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}
    
    .cursor {{
      animation: blink 0.9s infinite;
      fill: #ff79c6;
    }}

    .scanline {{
      fill: none;
      stroke: rgba(0, 242, 254, 0.15);
      stroke-width: 2;
      animation: scan 4s linear infinite;
    }}

    @keyframes typeIn {{
      0% {{ opacity: 0; transform: translateY(4px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes blink {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
    }}

    @keyframes scan {{
      0% {{ transform: translateY(0); }}
      100% {{ transform: translateY({height}px); }}
    }}
  </style>

  <!-- Background Card -->
  <rect class="card-bg" width="{width}" height="{height}" />
  <rect class="card-border" width="{width}" height="{height}" />

  <!-- Scanline effect -->
  <line x1="0" y1="0" x2="{width}" y2="0" class="scanline" />

  <!-- Window Header -->
  <rect class="title-bar" width="{width}" height="38" />
  <rect x="0" y="37" width="{width}" height="1" fill="#21263d" />
  <circle cx="20" cy="19" r="5" fill="#ff5f56" />
  <circle cx="36" cy="19" r="5" fill="#ffbd2e" />
  <circle cx="52" cy="19" r="5" fill="#27c93f" />
  <text x="72" y="23" class="title-text">⚡ {username}@terminal ~ avatar.sh</text>

  <!-- ASCII Art Lines -->
{chr(10).join(rows_xml)}

  <!-- Blinking Cursor -->
  <rect class="cursor" x="380" y="247" width="8" height="13" rx="1" />
</svg>'''

    with open("avadh-ascii.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Successfully generated ultra-animated avadh-ascii.svg")

if __name__ == "__main__":
    generate_ascii_svg()
