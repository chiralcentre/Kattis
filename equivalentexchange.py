from sys import stdin,stdout

d = int(stdin.readline())
mappings,i = {},0
# mappings[i] = list of days where item i was gathered
# code runs in O(d log d) as each element is moved at most (log d) times
for _ in range(d):
    q,*rest = map(int,stdin.readline().split())
    if q == 1:
        f = rest[0]
        if f not in mappings:
            mappings[f] = [i]
        else:
            mappings[f].append(i)
        i += 1
    else:
        s,e = rest
        if s not in mappings:
            continue
        a,b = mappings.pop(s),mappings.get(e,[])
        # ensure a is shorter than b
        if len(b) < len(a):
            a,b = b,a
        b.extend(a)
        mappings[e] = b
results = [None] * i
for key,values in mappings.items():
    for v in values:
        results[v] = str(key)
stdout.write("\n".join(results))
