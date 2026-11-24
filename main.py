"""Write the AI dating-bio entry to entry.txt in the output directory.

The output directory is $MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise /output. Standard library only, no network and no randomness.
"""

import os
import sys

TEXT = "My attachment style is scheduled, idempotent and exactly once. Four blind rounds went unrequited, and I've already saved you a seat at round five.\n"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

try:
    os.makedirs(output_dir, exist_ok=True)
except OSError as exc:
    sys.exit(f"cannot create output directory {output_dir!r}: {exc}")

with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
