from sys import stdin,stdout
from heapq import heappush,heappop

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    #use a max heap to store bids, and a min heap to store asks
    bids,asks = [],[]
    S = '-1' #S refers to last transaction price
    for i in range(n):
        order = stdin.readline().split()
        q,p = int(order[1]),int(order[4])
        if order[0] == "buy":
            heappush(bids,(-p,q)) #negate to convert to max heap
        else: #sell order
            heappush(asks,(p,q))
        while bids and asks and -bids[0][0] >= asks[0][0]: #sell order went through
            p1,q1 = heappop(bids); p2,q2 = heappop(asks); S = str(p2)
            # do nothing in equality case
            if q1 > q2:
                heappush(bids,(p1,q1-q2))
            elif q2 > q1:
                heappush(asks,(p2,q2-q1))
        A = str(asks[0][0]) if asks else '-'
        B = str(-bids[0][0]) if bids else '-'
        S = S if S != '-1' else '-'
        stdout.write(f"{A} {B} {S}\n")

