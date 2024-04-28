from sys import stdin

ans,best = "",-1
for _ in range(int(stdin.readline())):
    name,fun = stdin.readline().split()
    fun = int(fun)
    if fun > best:
        ans,best = name,fun
print(ans)