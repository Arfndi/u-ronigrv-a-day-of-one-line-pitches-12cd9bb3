# u-ronigrv-a-day-of-one-line-pitches-12cd9bb3 entry: one-sentence pitch.
#
# The pitch is a fixed string: the program is deterministic by construction,
# so two runs write the same bytes. It reads $MAKEFUN_OUTPUT_DIR when set,
# else /output, and writes entry.txt there.

import os

LINE = "Describe your idea in one sentence, watch an AI agent build it into a real app while you have coffee, and if you don't like it, describe it differently and watch it rebuild — no code, no cost, just your idea becoming something you can tap."

# The gate allows 1 to 240 characters, one sentence; refuse to write an
# over-long line rather than submit an entry the scorer would mark invalid.
# A newline would also break the one-line shape, so refuse that too.
MAX_CHARS = 240

def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(LINE)} chars, outside the 1-{MAX_CHARS} gate")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line")
    if LINE.count(".") != 1:
        raise SystemExit("entry must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
