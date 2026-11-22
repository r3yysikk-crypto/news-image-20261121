"""news-image-20261121: write one image summing up 21 November 2026's world news.

The image is bundled in this repo as entry.png (1024x1024 PNG, <1 MiB):
a newspaper front page for Saturday 21 November 2026 — Trump, Xi and Putin
meet at a trilateral summit in Shenzhen; a Russian missile lands in Poland
during strikes on Ukraine; tankers burn in the Strait of Hormuz; AI stocks
sell off and markets fall into correction; COP31 deadlocks over fossil
fuels; the ICJ rules on Myanmar and the Rohingya.
This program copies it byte-for-byte to /output/entry.png, then verifies
the copy matches the source. No network, no randomness: two runs write
identical bytes.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    src = os.path.join(HERE, "entry.png")
    dst = "/output/entry.png"
    if not os.path.isfile(src):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, dst)
    if sha256(src) != sha256(dst):
        print("copy mismatch: output differs from source", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
