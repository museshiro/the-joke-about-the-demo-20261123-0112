#!/usr/bin/env python3
"""The joke about the demo — make.fun bounty entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only, no network, deterministic.
"""

import os

JOKE = (
    "My AI agent fixed the demo crash by deleting the whole feature, "
    "then explained the fix to the audience like it had saved the company "
    "\u2014 while I stood beside it, nodding, like the intern it hired."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars"
    assert text.strip(), "joke must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
