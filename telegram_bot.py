import os
import requests
from datetime import datetime

# Read secrets from environment
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL = os.environ["TELEGRAM_CHANNEL"]

# Load all tips
with open("tips.txt", "r", encoding="utf-8") as f:
    tips = [line.strip() for line in f if line.strip()]

# Calculate run slot (e.g., Day * 2 + shift)
now = datetime.utcnow()
day_number = now.timetuple().tm_yday  # 1 to 366

# Shift: 0 = morning, 1 = evening
hour = now.hour
shift = 0 if hour < 12 else 1

# Final tip index (rotates twice daily)
index = ((day_number - 1) * 2 + shift) % len(tips)
tip = tips[index]

# Format message
message = f"💡 Daily Coding Tip #{index + 1}\n\n{tip}\n\n#Java #DSA #DevTips"

# Send to Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHANNEL, "text": message}
res = requests.post(url, data=payload)

print(f"✅ Sent Tip #{index + 1} to Telegram")
