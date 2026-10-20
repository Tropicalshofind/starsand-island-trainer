# Contributing to Starsand Island Trainer

Thanks for taking the time to help out. This is a hobbyist trainer for
**Starsand Island** — a single-player island survival / exploration game.
The trainer attaches to the local game process, reads a small set of
known offsets, and lets you tweak things like stamina, inventory stacks,
and time-of-day.

## Ground rules

- This is a **single-player only** project. Do not add features that
  target any multiplayer or online component.
- Keep memory offsets in `services/offset_registry.py` — never hardcode
  them in handlers.
- Every new handler must have a `dry_run` path that logs instead of
  writing to memory.
- Test with the game in **offline mode** before opening a PR.

## Local setup

```bat
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m starsand_trainer
```

## Pull requests

- One feature per PR.
- Update `services/offset_registry.py` and `docs` if you bump offsets
  for a new game patch.
- Run `pytest tests/` before submitting.

Have fun and don't break your save file.