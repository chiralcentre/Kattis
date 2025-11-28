from sys import stdin

n = int(stdin.readline())
chosen = set()
ans = []
for i in range(n):
    _,*apps = stdin.readline().split()
    for app in apps:
        if app not in chosen:
            ans.append(app)
            chosen.add(app)
            break
print(" ".join(ans))
