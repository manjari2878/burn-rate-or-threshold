# How I validated the simulator — my notes (Oct 14, 2026)

Files: `simulator.py` and `validate_simulator.py` in this folder.

Before using the simulator for the paper, I checked it on simple cases
which I can work out by hand: constant traffic (1,000 calls every
minute) and constant errors, so the correct paging minute is known.
This validation is reported in the paper (Method, Section 3.7).

## The hand-checked cases — all 10 passed

| Case | What I set up | Fixed line | Scaled line | Burn rate |
|---|---|---|---|---|
| V1 | 3% errors from minute 360, SLO 99.9 | page 367 | page 365 | page 388 |
| V2 | 0.5% errors throughout, SLO 99.0 | no page | no page | no page |
| V3 | 1% errors from minute 360, SLO 99.9 | never (miss) | page 367 | page 575 |
| V4 | 3% errors minutes 360–419 only, SLO 99.9 | page 367, recovers at 430, no second page | — | — |

One honest note, because this is what checking is for: in my first hand
calculations I assumed a window must be fully filled with incident
minutes before a rule can fire. That is not correct — the rate is
counted with call volumes, so a partly filled window also shows a
raised rate (example: 4 incident minutes in a 5-minute window at 3%
errors gives 2.4%, which is already above the 2% line). I corrected my
calculations for these ramp minutes. The code also keeps a very small
tolerance (1e-9) on the burn-rate comparison, so if the burn touches
the line exactly (like the 6.00x in V3 at minute 575), it counts as
fired. After these corrections, my hand calculations and the code
agree exactly on all 10 checks.

## Trial runs (constant traffic, 5,000 calls per minute)

- **Slow leak at 99.9** (this incident deserves a page, 10x burn): the
  fixed line **misses it fully** — 1% errors never cross its 2% line,
  and 12,415 requests failed (5.75% of the 30-day budget). Burn rate
  pages after 204 minutes. Scaled line pages in 6 minutes (only 382
  failures, 0.18% of budget).
- **Control run, no incident, at 99.9:** no rule pages even once at
  this constant volume. False pages should come when the real traffic
  has quiet minutes with very less calls — that is my hypothesis H3,
  and the real data runs will tell.
- **Sudden spike at 99.0:** fixed line pages in 4 minutes, scaled line
  in 5 minutes, burn rate **does not page**. This is by design: a
  10-minute spike spends only about 0.6% of the monthly budget at 99.0,
  and burn-rate alerts are built to ignore what is not threatening the
  budget. In my scoring, a spike counts as page-worthy, so this is
  noted as a burn-rate miss — it is a real point for the paper's
  decision table, and it also pushes against my hypothesis H1 (I
  expected the disagreement mainly on the slow leak). The real data
  runs will decide.

Status: the simulator is ready. The full grid — 18 scenarios, 30
repetitions each — runs after the Alibaba traffic data is extracted.
