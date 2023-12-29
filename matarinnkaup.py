from sys import stdin,stdout

n,k = map(int,stdin.readline().split())
recipes = {}
for _ in range(n):
    r = stdin.readline().strip()
    ingredients = {}
    for i in range(int(stdin.readline())):
        name,x = stdin.readline().split()
        x = int(x)
        ingredients[name] = x if name not in ingredients else ingredients[name] + x
    recipes[r] = ingredients

dishes,required = {},{}
for _ in range(k):
    for i in range(int(stdin.readline())):
        d,y = stdin.readline().split()
        y = int(y)
        dishes[d] = y if d not in dishes else dishes[d] + y

for k,v in dishes.items():
    tmp = recipes[k]
    for name in tmp:
        required[name] = v * tmp[name] if name not in required else required[name] + v * tmp[name]

stdout.write("\n".join(" ".join(str(elem) for elem in row) for row in sorted(required.items())))
