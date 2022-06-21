from sys import stdin,stdout

#greedy approach is employed here
for i in range(int(stdin.readline())):
    N,M,L = map(int,stdin.readline().split())
    agencies = []
    for _ in range(L):
        name,rest = stdin.readline().split(':')
        A,B = map(int,rest.split(','))
        start,cost = N,0
        while start > M: #O(log(N/M))
            #divide by 2 if it is possible to do so and it is cheaper to do so
            if start >= 2*M and A*(start - start//2) > B: 
                cost += B
                start //= 2
            else: #once it is no longer feasible to divide by 2, subtract by 1 all the way until M units are left
                cost += (start - M)*A
                start = M
        agencies.append((name,cost))
    #sort by cost and then by agency name in ascending order in O(L log L time)
    agencies.sort(key = lambda x: (x[1],x[0]))
    stdout.write(f"Case {i+1}\n")
    for name,cost in agencies:
        stdout.write(f"{name} {cost}\n")
