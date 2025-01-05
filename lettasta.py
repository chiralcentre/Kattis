from sys import stdin,stdout

N,M = int(stdin.readline()),int(stdin.readline())
problems = stdin.readline().split()
problem_scores = [0 for _ in range(N)]
for _ in range(M):
    scores = list(map(int,stdin.readline().split()))
    for i in range(N):
        problem_scores[i] += scores[i]
best,p_index = -1,0
for i in range(N):
    if problem_scores[i] > best:
        best,p_index = problem_scores[i],i
stdout.write(f"{problems[p_index]}\n")
