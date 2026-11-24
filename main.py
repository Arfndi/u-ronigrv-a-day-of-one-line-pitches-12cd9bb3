"""u-ronigrv-a-day-of-one-line-pitches-12cd9bb3 entry: writes the one-sentence pitch to entry.txt."""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

ENTRY = "Describe your idea in one sentence, watch an AI agent build it into a real app while you have coffee, and if you don't like it, describe it differently and watch it rebuild — no code, no cost, just your idea becoming something you can tap."
# Gate: 1-240 characters, single sentence; this entry is 239 characters.

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
