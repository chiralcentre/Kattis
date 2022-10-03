from sys import stdin,stdout

N = int(stdin.readline())
categories,associated = {},{}
for _ in range(N):
    c,w,*cats = stdin.readline().split()
    categories[c] = 0
    for cat in cats:
        if cat not in associated:
            associated[cat] = [c]
        else:
            associated[cat].append(c)

for line in stdin:
    words = line.split()
    for w in words:
        if w in associated:
            for cat in associated[w]:
                categories[cat] += 1

highest,bestCats = -1,[]
for key,value in categories.items():
    if value > highest:
        highest = value
        bestCats = [key]
    elif value == highest:
        bestCats.append(key)
stdout.write('\n'.join(c for c in sorted(bestCats)))
