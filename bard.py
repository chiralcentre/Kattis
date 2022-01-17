N,E = int(input()),int(input())
villagers = {num: set() for num in range(1,N+1)}
for I in range(E):
    line = list(map(int,input().split()))
    n,present = line[0],line[1:]
    if 1 in present:
        for num in present:
            villagers[num].add(I) #I stands for song number
    else:
        learned = villagers[present[0]]
        for j in range(1,n):
            learned = learned|villagers[present[j]] #union of songs learned
        for num in present:
            villagers[num] = set(x for x in learned) # make a deepcopy
# print out villagers who have learned the same songs as the bard
print('\n'.join(str(key) for key,value in villagers.items() if value == villagers[1]))
        
    
    
