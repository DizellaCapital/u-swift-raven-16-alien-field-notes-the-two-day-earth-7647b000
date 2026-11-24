"""Alien Field Notes: The Two Day Earth Review entry program.

Writes one alien tourist's review of planet Earth to
MAKEFUN_OUTPUT_DIR/entry.txt: a three-star review — lovely planet, bad
logistics — gravity drops the luggage, the weather changes four times
before lunch, and locals charge for water on a world that is 70%
water. The sunsets are worth it. One line, 197 characters, no
trailing newline. Stdlib only.
"""

import os
import sys

LINE = "Three stars. Lovely planet, bad logistics: gravity dropped my luggage twice, weather changed four times before lunch, and locals charge for water on a world that is 70% water. Sunsets are worth it."


def main():
    if not (1 <= len(LINE) <= 200):
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if "\t" in LINE:
        print("entry must not contain tabs", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
