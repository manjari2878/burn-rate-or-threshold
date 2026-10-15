"""
Run the full test grid for my ACMSE paper on the real traffic series.

The grid: 3 SLO targets x 3 incident shapes x 2 traffic levels
(busy start, quiet start) = 18 scenarios, each with 30 random seeds,
and all three paging rules tested on every run. Plus one control
pass per SLO with no incident at all -- every page there is a
false page.

The two start minutes come from my onset rule applied to the
extracted series (see hour_table.py): incidents start at an hour
start after the six-hour warm-up where even the four-hour slow
leak still fits inside the 12 hours. On this series that gives
busy start = minute 420 (hour 7) and quiet start = minute 480
(hour 8).

Input:  service_series.csv in this folder (from extract_service.py)
Output: results_grid.csv and results_control.csv in this folder

Author: Manjari Mettu
"""

import csv
import statistics

from simulator import run_scenario

BUSY_ONSET = 420
QUIET_ONSET = 480
SEEDS = range(1, 31)
SLOS = [0.990, 0.995, 0.999]
SHAPES = ["spike", "leak", "partial"]
TRAFFIC = [("busy", BUSY_ONSET), ("quiet", QUIET_ONSET)]
STRATEGIES = ["static", "burn", "scaled"]


def median_or_blank(values):
    values = [v for v in values if v is not None]
    return round(statistics.median(values), 2) if values else ""


def main():
    with open("service_series.csv") as f:
        rows = list(csv.reader(f))
    calls = [int(r[1]) for r in rows[1:]]
    assert len(calls) == 720, f"expected 720 minutes, got {len(calls)}"

    grid = []
    for slo in SLOS:
        for shape in SHAPES:
            for traffic, onset in TRAFFIC:
                runs = {s: [] for s in STRATEGIES}
                for seed in SEEDS:
                    out = run_scenario(calls, slo, shape, onset, seed)
                    for s in STRATEGIES:
                        runs[s].append(out[s])
                for s in STRATEGIES:
                    rs = runs[s]
                    grid.append({
                        "slo": slo, "shape": shape, "traffic": traffic,
                        "onset": onset, "strategy": s,
                        "page_worthy": rs[0]["page_worthy"],
                        "seeds_paged": sum(r["paged"] for r in rs),
                        "misses": sum(r["missed"] for r in rs),
                        "median_ttd_min": median_or_blank([r["ttd"] for r in rs]),
                        "median_harm_failed": median_or_blank([r["harm_failed"] for r in rs]),
                        "median_harm_budget_pct": median_or_blank([r["harm_budget_pct"] for r in rs]),
                        "median_pages": median_or_blank([r["n_pages"] for r in rs]),
                        "max_pages": max(r["n_pages"] for r in rs),
                    })
                print(f"SLO {slo}: {shape} @ {traffic} -- done")

    with open("results_grid.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(grid[0].keys()))
        w.writeheader()
        w.writerows(grid)

    control = []
    for slo in SLOS:
        runs = {s: [] for s in STRATEGIES}
        for seed in SEEDS:
            out = run_scenario(calls, slo, None, None, seed)
            for s in STRATEGIES:
                runs[s].append(out[s]["n_pages"])
        for s in STRATEGIES:
            control.append({
                "slo": slo, "strategy": s,
                "median_false_pages_per_12h": statistics.median(runs[s]),
                "max_false_pages_per_12h": max(runs[s]),
                "seeds_with_any_page": sum(1 for n in runs[s] if n > 0),
            })
        print(f"SLO {slo}: control (no incident) -- done")

    with open("results_control.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(control[0].keys()))
        w.writeheader()
        w.writerows(control)

    print()
    print("Wrote results_grid.csv (54 rows) and results_control.csv (9 rows).")


if __name__ == "__main__":
    main()
