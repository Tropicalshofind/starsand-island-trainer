# Security Policy

## Scope

`starsand-island-trainer` is a **local, single-player** memory trainer.
It does not phone home, does not ship a network client, and does not
modify game files on disk — everything happens in-process at runtime.

## Reporting a vulnerability

If you find something that could be abused beyond the intended
single-player scope (e.g. an accidental remote-code path in the
config loader), open a private security advisory on GitHub or email
`security@starsand-trainer.invalid`.

Please **do not** open a public issue for exploitable bugs.

## Out of scope

- Anti-cheat / online play — the trainer refuses to attach to any
  process whose executable name doesn't match the offline client.
- Save-file corruption caused by using debug flags — see README.
- "It doesn't work on patch X" — open a normal issue with the game
  build number and the failing offset.

## Supported builds

Only the latest stable Steam build is tested. Older builds may work
but offsets are not verified.