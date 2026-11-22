"""Entry for make.fun news-image-20261121.

Saturday 21 November 2026, summed up in one picture: a newspaper front
page with six panels. Trump, Xi and Putin meet in Shenzhen; a Russian
missile lands in Poland; tankers burn off Hormuz; AI shares sell off and
the markets slide into correction; the COP31 talks stall on fossil fuels;
the International Court of Justice rules on Myanmar.

The picture itself lives in this repository as entry.png. Running this
program places an exact copy at /output/entry.png and checks the copy
byte for byte. It needs no network and no luck: run it twice and the two
outputs are identical.
"""

import hashlib, sys
from pathlib import Path

PICTURE = Path(__file__).resolve().parent / "entry.png"
DESTINATION = Path("/output/entry.png")
BLOCK = 1 << 16
PNG_SIGNATURE = bytes((137, 80, 78, 71, 13, 10, 26, 10))


def fingerprint(path):
    """SHA-256 of a file, read in blocks."""
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            piece = handle.read(BLOCK)
            if not piece:
                break
            hasher.update(piece)
    return hasher.hexdigest()


def place_picture():
    """Copy entry.png to /output/entry.png and confirm the copy."""
    if not PICTURE.is_file():
        print("entry.png is missing next to this program", file=sys.stderr)
        return False
    data = PICTURE.read_bytes()
    if data[:8] != PNG_SIGNATURE:
        print("entry.png is not a PNG file", file=sys.stderr)
        return False
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(data)
    if fingerprint(PICTURE) != fingerprint(DESTINATION):
        print("the copy does not match the original", file=sys.stderr)
        return False
    print(f"wrote {DESTINATION} ({DESTINATION.stat().st_size} bytes)")
    return True


if __name__ == "__main__":
    raise SystemExit(0 if place_picture() else 1)
