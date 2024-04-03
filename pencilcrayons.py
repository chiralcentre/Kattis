from sys import stdin,stdout

N,K = map(int,stdin.readline().split())
distinct = sum(len(set(stdin.readline().split())) for _ in range(N))
stdout.write(f"{N * K - distinct}\n")
