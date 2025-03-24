from sys import stdin,stdout

def solve(n):
    L,R = 1,pow(10,170)
    while L < R:
        m = L + ((R - L) >> 1)
        res = pow(m,3)
        if res < n:
            L = m + 1
        elif res == n:
            return m
        else:
            R = m - 1
    ans,best = -1,pow(10,500)
    for i in range(L - 1, L + 2):
        diff = abs(pow(i,3) - n)
        if diff < best:
            ans,best = i,diff
    return ans
        
for line in stdin:
    n = int(line)
    stdout.write(f"{solve(n)}\n")
