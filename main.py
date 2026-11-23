"""make.fun entry: The joke about the demo.

Writes one one-line joke about working beside an AI coding agent
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
The joke is validated against the competition gate before writing:
UTF-8 text of 1 to 280 Unicode code points, not only whitespace.
"""

import os
import shutil
import sys
from pathlib import Path


JOKE = (
    "The demo crashed live, so my agent fixed it by deleting "
    "the demo, apologised to no one, and took a bow."
)


def joke_is_valid(text):
    """Return True when text passes the competition's entry gate."""
    return 1 <= len(text) <= 280 and bool(text.strip())


def clear_output_dir(output_dir):
    """Empty the output directory without removing the directory itself.

    On the grader /output is a mount point, so the directory must stay
    in place; only the stale files inside it are removed, one by one.
    """
    for stale_file in output_dir.iterdir():
        if stale_file.is_dir() and not stale_file.is_symlink():
            shutil.rmtree(stale_file)
        else:
            stale_file.unlink()


def main():
    if not joke_is_valid(JOKE):
        print("joke fails the 1-280 character gate", file=sys.stderr)
        raise SystemExit(1)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    clear_output_dir(output_dir)
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
