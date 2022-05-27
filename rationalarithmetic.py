from sys import stdin,stdout

def gcd(e,f):
    while f > 0:
      rem = e%f
      e = f
      f = rem
    return e

for _ in range(int(stdin.readline())):
    x1,y1,op,x2,y2 = stdin.readline().split()
    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
    if op == "/":
        denom = y1*x2; num = x1*y2
    else:
        denom = y1*y2
        if op == "+":
            num = x1*y2 + x2*y1
        elif op == "-":
            num = x1*y2 - x2*y1
        else: # multiplication operation
            num = x1*x2
    if denom < 0:
        num = -num; denom = -denom #denominator must be positive
    g = gcd(num,denom)
    num //= g; denom //= g
    stdout.write(f"{num} / {denom}\n")
