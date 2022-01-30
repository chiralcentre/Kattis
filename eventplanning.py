def find_hotel(options,B,N):
    while options: # start from cheapest hotel
        cost,capacity = options.pop(0)
        if max(capacity) >= N and N*cost <= B:
            return N*cost
    return "stay home"

N,B,H,W = map(int,input().split())
options = sorted([[int(input()),list(map(int,input().split()))] for _ in range(H)],key = lambda x: x[0])
print(find_hotel(options,B,N))
