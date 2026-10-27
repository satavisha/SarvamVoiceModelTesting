import os

from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

api_key = os.environ.get("SARVAM_API_KEY")
if not api_key:
    raise SystemExit("SARVAM_API_KEY is not set. Add it to .env and try again.")

client = SarvamAI(api_subscription_key=api_key)

response = client.chat.completions(
    messages=[{"role": "user", "content": "Hello, who are you?"}],
    model="sarvam-105b-conversations",
)

print(response.choices[0].message.content)
