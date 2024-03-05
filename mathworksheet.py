from sys import stdin,stdout

start = True
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    if start:
        start = False
    else:
        stdout.write("\n")
    res,longest = [],-1
    for _ in range(n):
        ans = str(eval(stdin.readline().strip()))
        res.append(ans)
        longest = max(longest, len(ans))
    s,length = 0,0
    while s < len(res):
        for k in range(longest - len(res[s])):
            stdout.write(" ")
        stdout.write(res[s])
        length += longest; s += 1
        if length + 1 + longest > 50 or s == len(res):
            stdout.write("\n")
            length = 0
        elif s < len(res):
            stdout.write(" ")
            length += 1
