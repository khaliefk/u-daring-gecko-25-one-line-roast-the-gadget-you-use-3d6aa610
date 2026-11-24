"""One-line roast entry for make.fun.

Writes a single original roast line about a gadget used every day
to /output/entry.txt. The line is one sentence, plain UTF-8 text,
no trailing newline.
"""

from pathlib import Path

ROAST = (
    "My earbuds die one at a time, so half my calls sound like "
    "a hostage negotiation over a walkie-talkie."
)


def main() -> None:
    text = ROAST.strip()
    # Gate the entry the same way the house scorer does: 1-200 chars,
    # one line, and it must read as a single finished sentence.
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text.count("\n") != 0:
        raise ValueError("entry must be a single line")
    if not text.endswith("."):
        raise ValueError("entry must end as one finished sentence")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
