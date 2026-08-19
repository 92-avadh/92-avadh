import json
import re
import os
import urllib.request

USERNAME = "andriidrok1"
URL = f"https://github.com/users/{USERNAME}/contributions"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def fetch():
    req = urllib.request.Request(URL, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching URL: {e}")
        html = ""

    # Parse days using regex for ContributionCalendar-day
    day_matches = re.findall(r'class="[^"]*ContributionCalendar-day[^"]*"[^>]*data-date="([^"]+)"[^>]*data-level="(\d+)"', html)
    
    if not day_matches:
        day_matches = re.findall(r'data-date="([^"]+)"[^>]*data-level="(\d+)"', html)

    days_data = []
    for date_str, level_str in day_matches:
        level = int(level_str)
        count = level * 2 if level > 0 else 0
        days_data.append({
            "date": date_str,
            "level": level,
            "count": count
        })

    days_data.sort(key=lambda d: d["date"])

    longest_streak = 0
    temp_streak = 0
    for day in days_data:
        if day["level"] > 0:
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0

    current_streak = 0
    for day in reversed(days_data):
        if day["level"] > 0:
            current_streak += 1
        else:
            break

    total_contributions = sum(d["count"] for d in days_data)

    output = {
        "username": USERNAME,
        "total_contributions": total_contributions,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "total_days": len(days_data),
        "days": days_data
    }

    os.makedirs("data", exist_ok=True)
    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Successfully saved {len(days_data)} contribution days for {USERNAME} (Total estimate: {total_contributions}).")

if __name__ == "__main__":
    fetch()
