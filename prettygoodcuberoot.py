from sys import stdin,stdout
from math import floor,ceil

for line in stdin:
    n = int(line)
    approx = pow(n,1 / 3)
    a,b = floor(approx),ceil(approx)
    d1,d2 = abs(n - pow(a,3)),abs(n - pow(b,3))
    if d1 < d2:
        stdout.write(f"{a}\n")
    else:
        stdout.write(f"{b}\n")
