import os
import requests
from datetime import datetime
import hashlib

# Read environment variables
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL = os.environ["TELEGRAM_CHANNEL"]

# Load and shuffle tips deterministically
with open("tips.txt", "r", encoding="utf-8") as f:
    tips = [line.strip() for line in f if line.strip()]

# Get current day and shift (AM/PM)
now = datetime.utcnow()
date_str = now.strftime("%Y-%m-%d")
shift = "AM" if now.hour < 12 else "PM"
key = f"{date_str}-{shift}"

# Deterministic shuffle using the key as seed
seed = int(hashlib.sha256(key.encode()).hexdigest(), 16)
tips_sorted = sorted(tips, key=lambda x: hashlib.sha256((x + key).encode()).hexdigest())

# Pick the first tip from shuffled list
tip = tips_sorted[0]
index = tips.index(tip)

# Format the message
message = f"💡 Daily Coding Tip #{index + 1}\n\n{tip}\n\n#Java #DSA #DevTips"

# Send to Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHANNEL, "text": message}
res = requests.post(url, data=payload)

print(f"✅ Sent Tip #{index + 1} to Telegram")

