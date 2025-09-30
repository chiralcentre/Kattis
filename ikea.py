from sys import stdin,stdout

k,n = int(stdin.readline()),int(stdin.readline())
items = []
for i in range(n):
    name,w = stdin.readline().split()
    w = int(w)
    items.append((w,name,i))

# filter by weight, break ties by order items appear
items.sort(key = lambda x: (x[0], x[2]))
floor = n // k
ceil = n // k + (n % k > 0)
ans,floor_total = [],0
for i in range(floor):
    floor_total += items[i][0]
    ans.append(items[i][1])
if n % k:
    next_floor_total = sum(items[j][0] for j in range(ceil,ceil + floor))
    ceil_total = floor_total + items[ceil - 1][0]
    if ceil_total < next_floor_total:
        ans.append(items[ceil - 1][1])
        stdout.write(f"{ceil_total}\n")
    else:
        stdout.write(f"{floor_total}\n")
else:
    stdout.write(f"{floor_total}\n")
    
for name in sorted(ans):
    stdout.write(f"{name}\n")
