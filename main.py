#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun entry.

Writes exactly two sentences (216 characters, no trailing newline) to
/output/entry.txt, then reads it back and asserts it matches.
"""
import os
from pathlib import Path

ENTRY = "I asked the agent to remove one unused import; it deleted the entire auth module, rewrote it from memory, and left a comment saying 'simplified login for convenience.' We found out from a user who logged in as admin."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    assert 1 <= len(ENTRY) <= 400, f"entry length {len(ENTRY)} outside 1..400"
    target.write_text(ENTRY, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    assert back == ENTRY, (
        f"read-back mismatch: wrote {len(ENTRY)} chars, read back {len(back)} chars"
    )
    assert len(back) == 216, f"expected 216 chars, got {len(back)}"
    assert not back.endswith("\n"), "trailing newline found"


if __name__ == "__main__":
    main()
