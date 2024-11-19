a = input().strip()
b = input().strip()
a1,a2 = map(int,a.split("."))
b1,b2 = map(int,b.split("."))
oa,ob = float(a),float(b)
# equality case does not occur
r1 = 1 if oa > ob else 2
r2 = 1 if (a1,a2) > (b1,b2) else 2 if (a1,a2) < (b1,b2) else 0
print("-1") if r1 != r2 else print(oa if oa > ob else ob)
