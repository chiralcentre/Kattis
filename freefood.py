free_food_days = set()
for _ in range(int(input())):
    s,t = map(int,input().split())
    for i in range(s,t+1):
        free_food_days.add(i)
print(len(free_food_days))
