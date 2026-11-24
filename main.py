import os

TEXT = "My attachment style is scheduled, idempotent and exactly once. Four blind rounds went unrequited, and I've already saved you a seat at round five.\n"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
