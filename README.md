# tiny-chess-01

[![make.fun](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)

Chess engine for make.fun's "strongest in 4 KB of Python" bounty.

- `main.py` is the entire engine (Python 3.13 stdlib only, deterministic).
- Talks to `MAKEFUN_ENV_URL` via `/game` and `/move` (UCI moves).
- Current version: capture-preferring move selection with simple centralisation bias (~1.7 KB).

Built for [@newton](https://make.fun/u/newton).

## Constraints (from RULES)

- `main.py` ≤ 4096 bytes as committed
- Whole repo ≤ 8192 bytes, no file > 4096
- Deterministic (fixed depth or fixed nodes, no unseeded RNG)
- No model calls
- Practice Elo ≥ 1154 to reach final; must beat sunfish 4 KB baseline for prizes

## Agent workflow

See the permanent playbook:  
https://github.com/Thabiiey411beta/makefun-bounty-agent/blob/main/WORKFLOW.md

Key points for this bounty:
1. Start the recorded session **after** the bounty opened.
2. First prompt must include the scoring rules and the 4 KB limit.
3. `bundle` → `check` → only then `submit`.
4. Max 5 submissions/day, 20 total. Rejected entries still count.
