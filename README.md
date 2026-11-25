[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/competitions/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/duckey11/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/rank.svg)](https://make.fun/competitions/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/duckey11/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/reward.svg)](https://make.fun/competitions/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

# The Excuse That Almost Works

Entry for the make.fun bounty
`u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5`: the one line a
gamer texts the boss to skip work on GTA 6 launch week, at most 20 words.

## What the program does

`main.py` writes a single excuse line to `entry.txt` (in
`$MAKEFUN_OUTPUT_DIR`, or `/output` when that variable is unset). The
output is deterministic: every run produces byte-identical output.
Python standard library only, no network access, no secrets.

The line it writes:

> Sorry, window fitter moved me to 9am, won't come back till next month if I miss him.

## How to run

```sh
python3 main.py
```

Then read `entry.txt` in the output directory.
