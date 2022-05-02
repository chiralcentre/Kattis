from sys import stdin,stdout

k,r = map(int,stdin.readline().split())
ingredients = list(map(int,stdin.readline().split()))
highest = -1
for i in range(r): #O(rk)
    *usage,cost = map(int,stdin.readline().split())
    s = min(ingredients[j]//usage[j] for j in range(k) if usage[j] > 0) #find the maximum number of smoothies which can be made
    if s*cost > highest:
        highest = s*cost
stdout.write(f'{highest}')
    
