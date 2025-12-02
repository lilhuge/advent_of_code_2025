import os
from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv()  # reads .env into environment vars

session = os.getenv("AOC_SESSION")
if not session:
    raise RuntimeError("Missing AOC_SESSION in .env")

url = "https://adventofcode.com/2025/day/1/input"
resp = requests.get(url, cookies={"session": session})
resp.raise_for_status()

Path("day01/input.txt").write_text(resp.text.rstrip() + "\n")
print("Saved input!")