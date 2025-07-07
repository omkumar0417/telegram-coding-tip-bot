import os
import requests

# Read your Telegram bot token and channel username from environment
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL = os.environ["TELEGRAM_CHANNEL"]  

# Read all tips
with open("tips.txt", "r", encoding="utf-8") as f:
    tips = [line.strip() for line in f if line.strip()]

# Track which tip was posted last
index_file = "last_tip_index.txt"
if os.path.exists(index_file):
    with open(index_file, "r") as f:
        last_index = int(f.read().strip())
else:
    last_index = -1

# Calculate next tip index
next_index = (last_index + 1) % len(tips)
tip = tips[next_index]

# Create the message text
message = f"💡 Daily Coding Tip #{next_index + 1}\n\n{tip}\n\n#Java #DSA #DevTips"

# Send message to Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHANNEL, "text": message}
res = requests.post(url, data=payload)

print("✅ Telegram Tip Sent")

# Save the updated index
with open(index_file, "w") as f:
    f.write(str(next_index))
