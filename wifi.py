from sys import stdin,stdout

def can_achieve_d(p,w,n):
    curr = p[0] + w
    #start off with 1 access point
    points = 1
    for i in range(1,len(p)):
        if abs(curr - p[i]) > w:
            curr = p[i] + w
            points += 1
            if points > n:
                return False
    return True

for _ in range(int(stdin.readline())):
    n,m = map(int,stdin.readline().split())
    p = sorted([int(stdin.readline()) for i in range(m)])
    # perform binary search on range
    L,H = 0, pow(10,6)
    ans = -1
    # perform 50 rounds of binary search, answer should converge
    # log2(1000000) ~= 20
    for i in range(50): 
        M = L + ((H - L) / 2)
        if can_achieve_d(p,M,n):
            H,ans = M,M
        else:
            L = M
    stdout.write(f"{ans:.1f}\n")
        
