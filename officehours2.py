from sys import stdin

days = ["Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"]
mappings = {days[i]: i for i in range(len(days))}
H = 24

def decode(t):
    return f"{days[t // H]} {t % H}"

avail = [set() for _ in range(H * 7)]
for i in range(int(stdin.readline())):
    name,day,_,*tr = stdin.readline().split()
    d = mappings[day]
    for r in tr:
        s,e = map(int,r.split("-"))
        s = d * H + s
        e = d * H + e
        for j in range(s,e):
            avail[j].add(name)

# use a double for loop to check every possible pair of timings\
# O(N^2) time worst case, length of avail is 168 max
best,ans = -1,None
for i in range(len(avail)):
    for j in range(i + 1, len(avail)):
        res = avail[i].union(avail[j])
        if len(res) > best:
            best = len(res)
            ans = (i,j)
print(decode(ans[0]))
print(decode(ans[1]))
