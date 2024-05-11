from sys import stdin,stdout

total_views = {}
for _ in range(int(stdin.readline())):
    name,views = stdin.readline().split()
    views = int(views)
    total_views[name] = total_views.get(name,0) + views

best,ans = -1,""
for key,value in total_views.items():
    if value > best:
        best,ans = value,key
stdout.write(ans)
