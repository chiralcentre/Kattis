from math import floor
parts = [0,0,0,0] #indices 0,1,2,3 represent T,B,L,R respectively
for _ in range(int(input())):
    sword = input().strip()
    for i in range(len(sword)):
        parts[i] += 1 if sword[i] == '0' else 0
TB,LR = parts[0]+parts[1], parts[2]+parts[3]
fixed = min(floor(TB/2),floor(LR/2))
print(f'{fixed} {TB-fixed*2} {LR-fixed*2}')

    
