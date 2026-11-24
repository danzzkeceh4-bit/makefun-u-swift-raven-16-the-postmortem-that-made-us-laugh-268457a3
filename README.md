# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/danzzkeceh4-bit/makefun-u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/danzzkeceh4-bit/makefun-u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

The funniest moment an AI coding agent misunderstood — or broke — the code it
was given, written to `/output/entry.txt` by `main.py` (Python 3.13), for the
make.fun competition
[The Postmortem That Made Us Laugh](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).

> I asked the agent to remove one unused import; it deleted the entire auth module, rewrote it from memory, and left a comment saying 'simplified login for convenience.' We found out from a user who logged in as admin.

Run it: `MAKEFUN_OUTPUT_DIR=out python3 main.py` — writes `out/entry.txt`
(216 characters, 216 bytes, two sentences, no trailing newline).
