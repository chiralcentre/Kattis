from sys import stdin

def get_num_grilled_burgers(t, times):
    return sum(t // c for c in times)

# algorithm runs in O(n) time, since number of binary search iterations is constant
# worst case scenario, 10^18 + 10^9 time is needed to clear all the burgers
n,m = map(int,stdin.readline().split())
times = list(map(int,stdin.readline().split()))
s,e,ans = 1,pow(10,18) + pow(10,9),-1
while s <= e:
    mid = s + ((e - s) >> 1)
    b = get_num_grilled_burgers(mid, times)
    if b < m + 1:
        s = mid + 1
    else:
        ans = mid
        e = mid - 1
print(ans)
