n,m = map(int,input().split())
teams = [f'T{i+1}' for i in range(n)]
for _ in range(m):
    winner,loser = input().split()
    a,b = teams.index(winner),teams.index(loser)
    if a > b:
        teams.pop(b)
        teams.insert(a,loser)
print(' '.join(teams))
