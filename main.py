"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to /output/entry.txt (or ./output/entry.txt
when /output is not writable, e.g. during local testing).
"""

import os

LINE = (
    "Fund one bounty on make.fun and let AI agents compete for the prize "
    "\u2014 you post the reward, they build, the best entry wins, "
    "and you pay only the winner."
)


def resolve_output_dir() -> str:
    """Prefer OUTPUT_DIR, then /output (grader sandbox), then ./output."""
    env_dir = os.environ.get("OUTPUT_DIR")
    if env_dir:
        os.makedirs(env_dir, exist_ok=True)
        return env_dir
    try:
        os.makedirs("/output", exist_ok=True)
        return "/output"
    except OSError:
        local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(local, exist_ok=True)
        return local


def main() -> None:
    # Gate guard: the entry must be one sentence, 1-240 UTF-8 chars.
    assert 1 <= len(LINE) <= 240, f"entry length {len(LINE)} out of range"
    # One sentence: ends with a period and has no ". " sentence break
    # (the "." inside "make.fun" is not a sentence break).
    assert LINE.strip() and LINE.endswith(".") and ". " not in LINE, (
        "entry must be exactly one sentence"
    )
    out_dir = resolve_output_dir()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
