import os
import requests

# Read secrets from environment
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL = os.environ["TELEGRAM_CHANNEL"]

# Load all tips
with open("tips.txt", "r", encoding="utf-8") as f:
    tips = [line.strip() for line in f if line.strip()]

# Load last posted index
index_file = "last_tip_index.txt"
if os.path.exists(index_file):
    with open(index_file, "r") as f:
        try:
            last_index = int(f.read().strip())
        except ValueError:
            last_index = -1
else:
    last_index = -1

# Get next tip in sequence
next_index = (last_index + 1) % len(tips)
tip = tips[next_index]

# Format the message
message = f"💡 Daily Coding Tip #{next_index + 1}\n\n{tip}\n\n#Java #DSA #DevTips"

# Send to Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHANNEL, "text": message}
res = requests.post(url, data=payload)

print(f"✅ Tip #{next_index + 1} sent to Telegram")

# Save updated index
with open(index_file, "w") as f:
    f.write(str(next_index))
