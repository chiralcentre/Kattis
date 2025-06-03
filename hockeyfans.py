from sys import stdin

# code runs in O(N log H) time where H is highest value in list of decibels
def is_possible(D,N,S,M,decibels):
    completed,progress = 0,0
    for i in range(N):
        if decibels[i] >= D:
            progress += 1
        else:
            progress = 0
        if progress == S:
            progress = 0
            completed += 1
    return completed >= M
    
N,S,M = map(int,stdin.readline().split())
decibels = list(map(int,stdin.readline().split()))
L,H,ans = pow(10,10),-1,None
for num in decibels:
    L,H = min(L,num),max(H,num)
while L <= H:
    C = L + ((H - L) >> 1)
    if is_possible(C,N,S,M,decibels):
        L = C + 1
        ans = C
    else:
        H = C - 1
print(ans)
