from sys import stdin,stdout

def satisfy_conds(K,N,scores):
    first,second,third = 0,0,0
    for s in scores:
        if s * 10 >= 7 * K:
            third += 1
        if s * 10 >= 8 * K:
            second += 1
        if s * 10 >= 9 * K:
            first += 1
    return first * 4 >= N and second * 2 >= N and third * 4 >= 3 * N

# time complexity O(N log T)
N,T = map(int,stdin.readline().split())
scores = [int(stdin.readline()) for _ in range(N)]
# use upper bound of 2 * T as it is possible largest integer satisfying conditions is greater than T
L,H,ans = 1,T << 1,-1
while L <= H:
    m = L + ((H - L) >> 1)
    if satisfy_conds(m,N,scores):
        ans,L = m,m + 1
    else:
        H = m - 1
stdout.write(f"{ans}\n")
