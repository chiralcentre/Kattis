from sys import stdin,stdout
n,k = map(int,stdin.readline().split())
lst = list(map(int,stdin.readline().split()))
ans = [str(lst[i]) for i in range(n) if not (i+1)%k]
stdout.write(' '.join(char for char in ans))
