from sys import stdin,stdout

n = int(stdin.readline()); stream = [-1 for _ in range(n)]
for _ in range(n):
    t,i = map(int,stdin.readline().split())
    stream[i-1] = t #offset by 1 due to zero indexing
lag,curr = 0,1
for i in range(n):
    if curr < stream[i]:
        lag += stream[i] - curr
        curr = stream[i]
    curr += 1 #1 second to play video
stdout.write(str(lag))
