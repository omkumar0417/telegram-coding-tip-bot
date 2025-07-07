# import os
# import requests
# from pathlib import Path

# # Read secrets from environment
# TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
# CHANNEL = os.environ["TELEGRAM_CHANNEL"]

# # Paths
# TIPS_FILE = "tips.txt"
# USED_FILE = "used_tips.txt"

# # Load tips
# all_tips = []
# with open(TIPS_FILE, "r", encoding="utf-8") as f:
#     all_tips = [line.strip() for line in f if line.strip()]

# # Load used tips
# Path(USED_FILE).touch()  # create if not exists
# with open(USED_FILE, "r", encoding="utf-8") as f:
#     used_tips = [line.strip() for line in f if line.strip()]

# # Filter unused tips
# unused_tips = [tip for tip in all_tips if tip not in used_tips]

# # Handle case where all tips are used
# if not unused_tips:
#     message = "✅ All tips used! Add more tips to tips.txt."
# else:
#     next_tip = unused_tips[0]
#     index = all_tips.index(next_tip) + 1
#     message = f"💡 Daily Coding Tip #{index}\n\n{next_tip}\n\n#Java #DSA #DevTips"

#     # Append to used tips
#     with open(USED_FILE, "a", encoding="utf-8") as f:
#         f.write(next_tip + "\n")

# # Send to Telegram
# if "✅ All tips used!" not in message:
#     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
#     payload = {"chat_id": CHANNEL, "text": message}
#     res = requests.post(url, data=payload)
#     print(f"✅ Sent Tip #{index} to Telegram")
# else:
#     print(message)
# import os
# import requests
# import random
# from datetime import datetime

# # Read environment secrets
# TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
# CHANNEL = os.environ["TELEGRAM_CHANNEL"]

# # Load all tips
# with open("tips.txt", "r", encoding="utf-8") as f:
#     tips = [line.strip() for line in f if line.strip()]

# # Use current UTC date and hour to create a deterministic random seed
# now = datetime.utcnow()
# day = now.timetuple().tm_yday  # 1-365
# shift = 0 if now.hour < 12 else 1
# seed = (day * 2 + shift)

# # Shuffle tips with consistent seed per time slot
# random.Random(seed).shuffle(tips)
# tip = tips[0]

# # Format and send the message
# message = f"💡 Daily Coding Tip #{seed % len(tips) + 1}\n\n{tip}\n\n#Java #DSA #DevTips"

# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
# payload = {"chat_id": CHANNEL, "text": message}
# res = requests.post(url, data=payload)

# print("✅ Tip sent:", tip)
import os
import requests
import random

# Read secrets from environment
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL = os.environ["TELEGRAM_CHANNEL"]

# Load all tips
with open("tips.txt", "r", encoding="utf-8") as f:
    tips = [line.strip() for line in f if line.strip()]

# Select a completely random tip
tip = random.choice(tips)

# Format message
message = f"💡 Daily Coding Tip\n\n{tip}\n\n#Java #DSA #DevTips"

# Send to Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHANNEL, "text": message}
res = requests.post(url, data=payload)

print("✅ Sent random tip to Telegram")
