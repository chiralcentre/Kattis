from sys import stdin,stdout

# use a bitmask to represent for each ingredient the subset of pizzas it is present in
# go through every pair of foreign word and native word to check if the bitmask are the same
for j in range(int(stdin.readline())):
    if j > 0:
        stdout.write("\n")
    n = int(stdin.readline())
    foreign,native = {},{}
    for i in range(n):
        pizza = stdin.readline().strip()
        m1,*items1 = stdin.readline().strip().split()
        m2,*items2 = stdin.readline().strip().split()
        for x in items1:
            if x not in foreign:
                foreign[x] = (1 << i)
            else:
                foreign[x] |= (1 << i)
        for y in items2:
            if y not in native:
                native[y] = (1 << i)
            else:
                native[y] |= (1 << i)
    pairs = []
    for k,v in foreign.items():
        for k2,v2 in native.items():
            if v == v2:
                pairs.append((k,k2))
    pairs.sort()
    for w1,w2 in pairs:
        stdout.write(f"({w1}, {w2})\n")

