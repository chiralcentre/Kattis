from math import ceil

B,Br,Bs,A,As = map(int,input().split())
Bm = (Br - B) * Bs
print(Bm // As + 1 + A)
