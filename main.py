"""Entry for make.fun: The Funniest Office Joke, Judged Head to Head.

Writes one short office joke to /output/entry.txt. The gate wants
UTF-8 text of 1 to 200 characters on a single line, so the program
checks its own line against that gate before writing it out.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The joke: a familiar office machine, a setup, and a turn at the end —
# the printer seems to know the narrator's mind before he does.
JOKE = (
    "The office printer printed my resignation letter again today. "
    "I never wrote one. It just knows things before I do."
)


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, outside the 1-200 gate")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
