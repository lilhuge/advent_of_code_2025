#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import requests
from dotenv import load_dotenv

TEMPLATE = """from pathlib import Path

def parse(path="input.txt"):
    return Path(path).read_text().strip().splitlines()

def part1(lines):
    # TODO
    return None

def part2(lines):
    # TODO
    return None

if __name__ == "__main__":
    data = parse()
    print("part1:", part1(data))
    print("part2:", part2(data))
"""

def main():
    load_dotenv()

    session = os.getenv("AOC_SESSION")
    year = os.getenv("AOC_YEAR", "2025")

    if not session:
        print("Missing AOC_SESSION in .env")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python new_day.py <day_number> [--open]")
        sys.exit(1)

    day = int(sys.argv[1])
    day_str = f"day{day:02d}"
    day_dir = Path(day_str)
    day_dir.mkdir(exist_ok=True)

    # write solve.py if not present
    solve_path = day_dir / "solve.py"
    if not solve_path.exists():
        solve_path.write_text(TEMPLATE)
        print(f"Created {solve_path}")

    # download input
    input_path = day_dir / "input.txt"
    if not input_path.exists() or input_path.stat().st_size == 0:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        r = requests.get(url, cookies={"session": session}, timeout=20)
        if r.status_code != 200:
            print(f"Failed to fetch input (HTTP {r.status_code}). Are you logged in / session valid?")
            print(r.text[:200])
            sys.exit(1)

        input_path.write_text(r.text.rstrip() + "\n")
        print(f"Downloaded input to {input_path}")
    else:
        print(f"Input already exists at {input_path}, skipping download.")

    # optionally open in editor
    if "--open" in sys.argv:
        # Try Cursor first, then VS Code
        os.system(f"cursor {solve_path} 2>/dev/null || code {solve_path}")

if __name__ == "__main__":
    main()
