n,p,m = list(map(int,input().split()))

players = {input().strip(): 0 for i in range(n)}

for j in range(m):
    name,points = input().split()
    players[name] += int(points)

found = False
for player in players:
    if players[player] >= p:
        found = True
        print(f'{player} wins!')

if not found:
    print("No winner!")
