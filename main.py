import os
import shutil
from pathlib import Path


JOKE = (
    "The demo crashed live, so my agent fixed it by deleting "
    "the demo, apologised to no one, and took a bow."
)


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    for stale_file in output_dir.iterdir():
        if stale_file.is_dir() and not stale_file.is_symlink():
            shutil.rmtree(stale_file)
        else:
            stale_file.unlink()
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
