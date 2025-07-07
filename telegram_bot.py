import os
import requests

# Telegram credentials
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL = os.environ["TELEGRAM_CHANNEL"]

TIPS_FILE = "tips.txt"
USED_FILE = "used.txt"

# Read tips
with open(TIPS_FILE, "r", encoding="utf-8") as f:
    tips = [line.strip() for line in f if line.strip()]

if not tips:
    print("⚠️ No tips left to post!")
    exit(0)

# Get the next tip
tip = tips[0]

# Update tips.txt to remove posted tip
with open(TIPS_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(tips[1:]))

# Append to used.txt
with open(USED_FILE, "a", encoding="utf-8") as f:
    f.write(tip + "\n")

# Build message
index = sum(1 for line in open(USED_FILE, "r", encoding="utf-8"))
message = (
    f"💡 Daily Coding Tip #{index}\n\n"
    f"{tip}\n\n"
    f"#Java #DSA #DevTips"
)

# Send to Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHANNEL, "text": message}
res = requests.post(url, data=payload)

print(f"✅ Tip #{index} sent to Telegram")
