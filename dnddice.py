t,c,o,d,u = map(int,input().split())
dies = []
for j in range(t):
    dies.append({i: 1 for i in range(1,5)})
for j in range(c):
    dies.append({i: 1 for i in range(1,7)})
for j in range(o):
    dies.append({i: 1 for i in range(1,9)})
for j in range(d):
    dies.append({i: 1 for i in range(1,13)})
for j in range(u):
    dies.append({i: 1 for i in range(1,21)})
results = dies[0]
for j in range(1,len(dies)):
    temp = {}
    roll = dies[j]
    for key in results:
        for face in roll:
            temp[key + face] = temp.get(key + face, 0) + results[key]
    results = temp
sorted_probs = sorted(results.items(), key = lambda x: -x[1])
print(" ".join(str(pair[0]) for pair in sorted_probs))
