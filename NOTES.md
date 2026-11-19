# tiny-chess-01 build notes

## Current engine (v1)
- Size: ~1.7 KB
- Strength: improved 1-ply (MVV-style captures + centralisation PST)
- Deterministic, no network except the env
- Plenty of headroom (~2.3 KB) for real search

## Next improvements (priority order)
1. Compact board + make/unmake + legal-move generation that stays under the byte budget
2. Alpha-beta or MTD-bi with fixed node budget (e.g. 20k–80k nodes)
3. Better PST / material + simple mobility or king safety
4. Quiescence or capture-only second ply when quiet
5. Keep everything pure stdlib and deterministic

## Interface reminder
```
POST $MAKEFUN_ENV_URL/game  {}           → {status, game, fen, legal_moves, ...}
POST $MAKEFUN_ENV_URL/move  {game, move} → next state or outcome
```
Loop until status == "done".

## Workflow reminder
Never submit without:
```
node cli/makefun.mjs bundle ...
node cli/makefun.mjs check ...
```
Sessions that started before the bounty opened are invalid for paid places.
