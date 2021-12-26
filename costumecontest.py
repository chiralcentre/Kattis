categories = {}

for i in range(int(input())):
    costume = input().strip()
    categories[costume] = 1 if costume not in categories else categories[costume] + 1

for key,value in sorted(categories.items()):
    if value == min(categories.values()):
        print(key) 
