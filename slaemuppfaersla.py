from sys import stdin

def main():
    N = int(stdin.readline())
    M = [int(stdin.readline()) for _ in range(N)]
    # prefix[i] = total updates before employee i
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + M[i]
    S = prefix[N]
    lo, hi = 0, S - 1
    while lo < hi:
        mid = (lo + hi) // 2
        out = []
        for i in range(N):
            if prefix[i+1] - 1 <= mid:
                out.append(M[i])                  # all updates for this employee
            elif prefix[i] > mid:
                out.append(0)                     # none
            else:
                out.append(mid - prefix[i] + 1)  # partial
        print(f"? {' '.join(map(str, out))}", flush=True)
        if stdin.readline().strip() == "Villa":
            hi = mid
        else:
            lo = mid + 1
    for i in range(N):
        if prefix[i] <= lo < prefix[i+1]:
            print(f"! {i+1} {lo - prefix[i] + 1}", flush=True)
            return

main()
