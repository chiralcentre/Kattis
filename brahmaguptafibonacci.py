a,b,c,d = map(int,input().split())
p = (a * a + b * b) * (c * c + d * d)
r1 = a * c - b * d
r2 = a * d + b * c
r3 = a * c + b * d
r4 = a * d - b * c
a1 = str(r1) if r1 >= 0 else f"({r1})"
a2 = str(r4) if r4 >= 0 else f"({r4})"
print(f"{a1}^2 + {r2}^2 = {p}")
print(f"{r3}^2 + {a2}^2 = {p}")