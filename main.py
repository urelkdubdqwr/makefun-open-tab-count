"""Write the makefun entry (a tab count) to <output dir>/entry.txt.

Output directory: $MAKEFUN_OUTPUT_DIR when set and non-empty, else /output.
The directory is created if missing. Standard library only.
"""
import os
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        sys.stderr.write("cannot create output directory %r: %s\n" % (out_dir, exc))
        raise SystemExit(1)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write("2143\n")


if __name__ == "__main__":
    main()
