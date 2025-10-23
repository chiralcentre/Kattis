line = input().strip()
A,Z = line.split("+")
X,Y = map(int,A.split("d"))
Z = int(Z)
E = ((Y * (Y + 1)) >> 1) / Y
print(E * X + Z)
