n = int(input())

dict1 = {}
players = list(map(int,input().split()))
for outcome in players:
    dict1[outcome] = 1 if outcome not in dict1 else dict1[outcome] + 1

unique = list(filter(lambda x: x[1] == 1, dict1.items()))
values = list(map(lambda x: x[0],unique))

print(players.index(max(values)) + 1) if len(values) > 0 else print('none')
    
    
