from sys import stdin,stdout
N,M = map(int,stdin.readline().split())
success_factor,popularity_factor = [i for i in range(1,N+1)],[0 for i in range(N)]
for _ in range(M):
    a,b = map(int,stdin.readline().split())
    popularity_factor[a-1] += 1
    popularity_factor[b-1] += 1
    
stdout.write(' '.join(str(popularity_factor[j]-success_factor[j]) for j in range(N)))
