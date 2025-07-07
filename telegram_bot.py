import os
import requests
import hashlib

# Telegram credentials
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL = os.environ["TELEGRAM_CHANNEL"]

# Load tips
with open("tips.txt", "r", encoding="utf-8") as f:
    tips = [line.strip() for line in f if line.strip()]

# Load used tip hashes
used_path = "used_ids.txt"
if os.path.exists(used_path):
    with open(used_path, "r") as f:
        used_ids = set(line.strip() for line in f)
else:
    used_ids = set()

# Function to hash tips
def tip_hash(tip):
    return hashlib.md5(tip.encode("utf-8")).hexdigest()

# Filter unused tips
unused = [(i, tip) for i, tip in enumerate(tips) if tip_hash(tip) not in used_ids]

if not unused:
    print("🎉 All tips have been used.")
    exit()

# Pick first unused tip (you can randomize if preferred)
index, tip = unused[0]
tip_id = tip_hash(tip)

# Append the used tip hash
with open(used_path, "a", encoding="utf-8") as f:
    f.write(tip_id + "\n")

# Format message
message = f"💡 Daily Coding Tip #{len(used_ids) + 1}\n\n{tip}\n\n#Java #DSA #DevTips"

# Send to Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHANNEL, "text": message}
requests.post(url, data=payload)

print(f"✅ Tip #{len(used_ids) + 1} sent.")
