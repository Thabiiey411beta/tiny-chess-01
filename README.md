# tiny-chess-01

[![make.fun](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)

Chess engine for make.fun's "strongest in 4 KB of Python" bounty.

- `main.py` is the entire engine (stdlib only, deterministic).
- Talks to `MAKEFUN_ENV_URL` via `/game` and `/move`.
- Currently: capture-preferring move selection with simple PST centralisation bias.

Built for [@newton](https://make.fun/u/newton).
