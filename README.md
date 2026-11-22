# tiny-chess-01

Chess engine for make.fun's strongest in 4 KB of Python bounty.

- `main.py` is the whole engine: Python 3.13 stdlib only, deterministic.
- 0x88 board, alpha-beta with iterative deepening (depth 1-9), fixed node budget (350,000 middlegame / 500,000 endgame), capture quiescence, transposition table (incremental Zobrist hash), killer + history ordering, null-move pruning, late-move reductions, futility pruning at low depth, material + PST eval with an endgame mating term.
- Talks to `MAKEFUN_ENV_URL` via `/game` and `/move` (UCI moves).
- Practice trial-0: 3 wins, 0 draws, 3 losses (beats depth-2, depth-3, depth-4 house engines), Elo ~1280, above the 1,154 practice floor.
- Practice Elo floor 1,154; must beat sunfish 4 KB baseline for prizes.
- Max 5 submissions/day, 10 total.
