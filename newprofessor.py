from sys import stdin
from heapq import heapify,heappop,heappush

# code runs in (CS log C) time
C = int(stdin.readline())
# use negation to convert min to max heap
freq = [-int(stdin.readline()) for _ in range(C)]
heapify(freq)
ans = 0
while len(freq) >= 5:
    top_five = [heappop(freq) for _ in range(5)]
    for f in top_five:
        if f != -1:
            heappush(freq,f + 1)
    ans += 5
ans += len(freq)
print(ans)
