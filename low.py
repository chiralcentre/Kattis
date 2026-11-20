from sys import stdin

# Let P(d) be the proposition that there exists an allocation of batteries whose maximum per machine difference <= d
# P(d) is true -> P(a) is true for all a >= d
def is_possible(batteries,n,k,d):
    i = opened = free = 0
    slots = 2 * k - 2 # filler capacity per machine opened
    while i < len(batteries):
        # open a new machine on (p[i], p[i+1]) when that pair is legal
        if opened < n and i + 1 < len(batteries) and batteries[i + 1] - batteries[i] <= d:
            opened += 1
            free += slots # capacity appears only now, to the left of all later batteries
            i += 2
        else:
            # p[i] can't start a pair -> forced filler, needs an already open machine
            if free == 0:
                return False
            free -= 1
            i += 1
    return True # surviving the sweep implies opened == n

# code runs in O(n log n + n log(10^9)) = O(n log n) 
n,k = map(int,stdin.readline().split())
batteries = sorted(map(int,stdin.readline().split()))
L,H,ans = 0,pow(10,9),None
while L <= H:
    M = L + ((H - L) >> 1)
    if is_possible(batteries,n,k,M):
        ans = M
        H = M - 1
    else:
        L = M + 1
print(ans)
