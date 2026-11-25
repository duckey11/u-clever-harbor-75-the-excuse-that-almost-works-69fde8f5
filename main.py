#!/usr/bin/env python3
"""Write the excuse line to entry.txt.

The program is deterministic: every run writes the exact same bytes.
It writes to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set,
otherwise to /output/entry.txt. Python standard library only, no
network access, no secrets.
"""

import os

ENTRY = "Sorry, window fitter moved me to 9am, won't come back till next month if I miss him."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
