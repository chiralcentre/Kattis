from sys import stdin,stdout

def euclidean_distance_squared(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

P,N = map(int,stdin.readline().split())
answer = set(); METRE_SQUARED = 10**6
#sort ping by times in O(N log N) time
pings = sorted([tuple(map(int,stdin.readline().split())) for _ in range(N)],key = lambda x: x[3])
if len(pings) <= 5:
    for j in range(len(pings)):
        for k in range(j+1,len(pings)):
            p1,x1,y1,t1 = pings[j]
            p2,x2,y2,t2 = pings[k]
            if p1 != p2 and t2 - t1 <= 10 and euclidean_distance_squared(x1,y1,x2,y2) <= METRE_SQUARED:
                answer.add((p1,p2)) if p1 < p2 else answer.add((p2,p1))
else:
    for i in range(len(pings)-5):
        for j in range(5):
            for k in range(j+1,5):
                p1,x1,y1,t1 = pings[i+j]
                p2,x2,y2,t2 = pings[i+k]
                if p1 != p2 and t2 - t1 <= 10 and euclidean_distance_squared(x1,y1,x2,y2) <= METRE_SQUARED:
                    answer.add((p1,p2)) if p1 < p2 else answer.add((p2,p1))

stdout.write(f"{len(answer)}\n")
for p1,p2 in sorted(answer,key = lambda x: (x[0],x[1])):
    stdout.write(f"{p1} {p2}\n")
