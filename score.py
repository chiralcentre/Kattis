from sys import stdin,stdout

def parseToSeconds(time):
    a,b = map(int,time.split(":"))
    return 60 * a + b

def convertToString(t):
    m,s = t//60, t%60
    first = str(m)
    second = str(s) if s >= 10 else f"0{s}"
    return f"{first}:{second}"

n = int(stdin.readline())
points,L = {"H": 0, "A": 0},{"H": 0, "A": 0}
prev,leader = -1,""
for i in range(n):
    T,p,time = stdin.readline().split()
    p,t = int(p),parseToSeconds(time)
    points[T] += p
    if leader:
        L[leader] += t - prev
    if points["H"] > points["A"]:
        leader = "H"
    elif points["H"] < points["A"]:
        leader = "A"
    else:
        leader = ""
    prev = t
L[leader] += 1920 - prev
ans = ["A" if points["A"] > points["H"] else "H"]
for key in L:
    ans.append(convertToString(L[key]))
stdout.write(" ".join(thing for thing in ans))
    
