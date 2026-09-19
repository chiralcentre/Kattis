# Find smallest t s.t. t + f(t) = T
# Define g(t) = f(t) + t - T = (t - a)^6 + (t - b)^4 + (t - c)^2 + d + t - T
# g'(t) = 6(t - a)^5 + 4(t - b)^3 + 2(t - c) + 1
# g''(t) = 30(t - a)^4 + 12(t - b)^2 + 2 > 0 for all t
# g is strictly convex
# g has at most two roots, and g' is strictly increasing, so we can find local minimiser for g by bisecting on g' to find where g'(t) = 0
# Left of the minimiser g is decreasing, and right of it g is increasing. Each side has at most one root, and bisection works on each side because of monotonicity
def solve(a,b,c,d,T):
    g  = lambda t: t + pow(t - a,6) + pow(t - b, 4) + pow(t - c, 2) + d - T
    dg = lambda t: 1 + 6 * pow(t - a, 5) + 4 * pow(t - b, 3) + 2 * (t - c)

    # Find minimiser of g on [0, inf)
    # If g'(0) >= 0, g is already increasing at 0, so minimiser m = 0
    if dg(0.0) >= 0:
        m = 0.0
    else:
        # g'(1000) > 0 as a,b,c <= 1000
        lo, hi = 0.0, 1000.0
        # 100 iterations of bisection
        for _ in range(100):
            mid = (lo + hi) / 2
            if dg(mid) < 0:
                lo = mid
            else:
                hi = mid
        m = hi
    # minimum above zero, no solution
    if g(m) > 0:
        return "O nei!"
    # bisect on the monotone piece containing the smallest root
    if g(0) >= 0:                   # decreasing on [0, m]
        lo, hi = 0.0, m
        for _ in range(100):
            mid = (lo + hi) / 2
            if g(mid) > 0:
                lo = mid
            else:
                hi = mid
    else:                             # increasing on [m, T]
        lo, hi = m, T
        for _ in range(100):
            mid = (lo + hi) / 2
            if g(mid) < 0:
                lo = mid
            else:
                hi = mid
    return(lo + hi) / 2

T = float(input())
a,b,c,d = map(float,input().split())
print(solve(a,b,c,d,T))
