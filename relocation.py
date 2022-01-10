N,Q = map(int,input().split())
companies = list(map(int,input().split()))
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1: #update
        companies[query[1]-1] = query[2]
    else: #query for distance
        print(abs(companies[query[1]-1]-companies[query[2]-1]))
