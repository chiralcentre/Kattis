from sys import stdin

def can_partition(weights,k,limit):
    boxes,curr = 1,0
    for w in weights:
        if curr + w <= limit:
            curr += w
        else:
            boxes += 1
            curr = w
    return boxes <= k

# binary search over range of weights in O(n log(n*w))
def solve(weights,k):
    L,H,ans = -1,0,None
    for w in weights:
        L = max(L,w)
        H += w
    while L <= H:
        M = (L + H) >> 1
        if can_partition(weights,k,M):
            ans = M
            H = M - 1
        else:
            L = M + 1
    return ans
            
n,k = map(int,stdin.readline().split())
weights = list(map(int,stdin.readline().split()))
print(solve(weights,k))
