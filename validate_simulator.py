"""
How I validated the simulator before trusting it.

I worked out these cases by hand first. Each case keeps the traffic
constant (1000 calls every minute, 720 minutes) and the errors also
constant and fixed -- no randomness -- so I can calculate myself at
which minute each rule should page. Then I run the code and check it
gives the same minutes. This validation is reported in the paper
(Method, Section 3.7).

My hand calculations
--------------------
Note: a window which is only partly filled with incident minutes also
shows a raised rate, because the rate is counted with call volumes.
Those "ramp" minutes are included in the calculations below -- in my
first attempt I forgot them and got different answers, then I fixed
my calculations. A real monitoring tool behaves the same way, so the
code was right and my first hand calculation was the wrong one.

V1: 3% errors from minute 360, SLO 99.9% (budget 0.1%).
    fixed line (5-min rate > 2%, sustained 5 minutes): the 5-minute
        rate first crosses 2% at minute 363 (4 incident minutes:
        120/5000 = 2.4%). The 5th minute together is 367 -> page 367.
    scaled line (6 x 0.1% = 0.6%): at minute 360 the rate is exactly
        0.6% (30/5000) and "crosses" means strictly more, so it first
        crosses at 361 (1.2%). 5th minute together -> page 365.
    burn rate, fast rule: 1-hour rate = (29 x 30)/(60 x 1000) = 1.45%
        >= 1.44% first at minute 388 (29 incident minutes inside the
        window); the 5-minute burn there is 30x. The slow rule needs
        216 incident minutes in the 6-hour window (minute 575), so the
        overall page is 388.
V2: 0.5% errors throughout, SLO 99.0% (budget 1%). Every window rate
    is 0.5% only: below the 2% fixed line, below the 6% scaled line,
    burn is 0.5x -> nobody pages.
V3: 1% errors from minute 360, SLO 99.9%.
    fixed line: 1% < 2% -> never pages (this is a miss).
    scaled line (0.6%): rate first crosses 0.6% at minute 363
        (4 incident minutes: 40/5000 = 0.8%) -> page 367.
    burn rate: fast rule is not possible (1% < 1.44% even with a full
        window). Slow rule: 6-hour rate = k/36000 >= 0.6% first at
        k = 216 incident minutes -> minute 575; the 30-minute rate is
        1% >= 0.6% -> page 575.
V4: 3% errors only in minutes 360-419, SLO 99.9%: fixed line pages at
    367 (same like V1). After the incident, the 5-minute rate goes
    below 2% from minute 421 and stays below, so the rule recovers at
    minute 430 and does not page again -> pages [367] only.
"""

import numpy as np

from simulator import make_strategies

CALLS = np.full(720, 1000)


def series_with_errors(spans):
    """spans: list of (start, end_inclusive, failures_per_minute)."""
    failures = np.zeros(720, dtype=int)
    for start, end, per_min in spans:
        failures[start:end + 1] = per_min
    return failures


def pages_for(failures, slo):
    return {s.name: s.run(failures, CALLS, slo) for s in make_strategies()}


def check(label, got, expected):
    ok = got == expected
    print(f"{'PASS' if ok else 'FAIL'}  {label}: got {got}, expected {expected}")
    return ok


def main():
    results = []

    v1 = pages_for(series_with_errors([(360, 719, 30)]), 0.999)
    results.append(check("V1 static", v1["static"], [367]))
    results.append(check("V1 scaled", v1["scaled"], [365]))
    results.append(check("V1 burn", v1["burn"], [388]))

    v2 = pages_for(series_with_errors([(0, 719, 5)]), 0.990)
    results.append(check("V2 static", v2["static"], []))
    results.append(check("V2 scaled", v2["scaled"], []))
    results.append(check("V2 burn", v2["burn"], []))

    v3 = pages_for(series_with_errors([(360, 719, 10)]), 0.999)
    results.append(check("V3 static", v3["static"], []))
    results.append(check("V3 scaled", v3["scaled"], [367]))
    results.append(check("V3 burn", v3["burn"], [575]))

    v4 = pages_for(series_with_errors([(360, 419, 30)]), 0.999)
    results.append(check("V4 static (page + recovery)", v4["static"], [367]))

    print()
    print("ALL PASS" if all(results) else "SOME CHECKS FAILED")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
