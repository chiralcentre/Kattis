from math import ceil,floor,log,exp,sqrt

# Instead of binary searching on the real value directly,
# the code maps [0, 10⁹] into ~16.7 million integer bins where any two adjacent bins are guaranteed to be within tolerance of each other.
EPS  = 1e-6
STEP = 1.3e-6 # ≤ 2·EPS, so half-step ≤ EPS = 1e-6
M_ABS = ceil(1.0 / STEP)
N_GEO = floor(log(1e9) / STEP)
TOTAL = M_ABS + N_GEO

# Linear regime (bins 0 … M_ABS, covering values 0 → 1)
# Bins are evenly spaced at 1.3×10^(-6) apart, satisfying the absolute error criterion near zero
# Geometric regime (bins M_ABS+1 … TOTAL, covering values 1 → 10^9)
# Bins are multiplicatively spaced — each is e^STEP ≈ 1 + 1.3×10^(-6) times the last — satisfying the relative error criterion for large numbers.
# Total number of bins = TOTAL = M_ABS + N_GEO ≈ 769231 + 15941743 ≈ 16710974 < 2^24
def pos_to_value(p):
    if p <= 0:        return 0.0
    if p <= M_ABS:    return p * STEP
    return exp((p - M_ABS) * STEP)

def ask(g):
    print(f"? {g}", flush=True)
    return input().strip().lower()

def solve():
    lo, hi = 0, TOTAL
    # 23 narrowing queries on the bin index
    for _ in range(23):
        if lo >= hi:
            break
        mid = (lo + hi) // 2
        r = ask(pos_to_value(mid))
        if "correct" in r or "close" in r or r == "-1":
            return
        if "low" in r:
            lo = mid + 1
        else:
            hi = mid - 1
    # 24th query: geometric mean of remaining bin values
    # The geometric mean is the right "midpoint" in the multiplicative regime, it minimises the maximum relative error between a and b
    a, b = pos_to_value(lo), pos_to_value(hi)
    if a <= 0 or b <= 0:
        g = (a + b) / 2                      # at least one is in the linear regime
    else:
        g = sqrt(a * b)
    ask(min(max(g, 0.0), 1e9))

solve()
