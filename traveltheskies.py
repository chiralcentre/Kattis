from sys import stdin,stdout

def optimalFlightPlan(flights,airports,arrivals,n,k):
    for d in range(n):
        for a,c in arrivals[d]:
            airports[a] += c
        for start,end,capacity in flights[d]:
            #check if existing customers at airport are sufficient without transferring the customers yet
            #since every customer can only have one flight a day
            if airports[start] < capacity: 
                return "suboptimal"
            else:
                airports[start] -= capacity
        for start,end,capacity in flights[d]: #update airport capacity on second iteration
            airports[end] += capacity
    return "optimal"
    
k,n,m = map(int,stdin.readline().split())
flights = [[] for j in range(n)] #store flights as edge list
arrivals,airports = [[] for i in range(n)],[0 for _ in range(k)]
for i in range(m):
    u,v,d,z = map(int,stdin.readline().split())
    flights[d-1].append((u-1,v-1,z)) #zero indexing
for j in range(k*n):
    a,b,c = map(int,stdin.readline().split())
    arrivals[b-1].append((a-1,c))
stdout.write(optimalFlightPlan(flights,airports,arrivals,n,k))
