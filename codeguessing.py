p,q = map(int,input().split())
Alice = [p,q] if q < p else [q,p]
positions = list(input().strip())
for i in range(4):
    if positions[i] == 'A':
        positions[i] = Alice.pop()
#brute force
possible_combinations = []
for i in range(1,10):
    for j in range(i+1,10):
        if i not in [p,q] and j not in [p,q]:
            temp = [x for x in positions]
            Bob = [j,i]
            for k in range(4):
                if temp[k] == 'B':
                    temp[k] = Bob.pop()
            if sorted(temp) == temp:
                possible_combinations.append((i,j))
print(' '.join(str(d) for d in possible_combinations[0])) if len(possible_combinations) == 1 else print(-1)
        
