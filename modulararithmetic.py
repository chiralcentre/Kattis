from sys import stdin,stdout

#Credits to CP4 repo for source code
def mod(a, m):
    return ((a % m) + m) % m

def modPow(b, p, m):
    if p == 0:
        return 1
    ans = modPow(b, p//2, m)
    ans = mod(ans*ans, m)
    if p % 2 == 1:
        ans = mod(ans*b, m)
    return ans

def extEuclid(a, b):
    xx, yy = 0, 1
    x, y = 1, 0
    while b != 0:
        q = a//b
        a, b = b, a%b
        x, xx = xx, x-q*xx
        y, yy = yy, y-q*yy
    return a, x, y


def modInverse(b, m):
    d, x, y = extEuclid(b, m)
    if d != 1:
        return -1
    return mod(x, m)

while True:
    n,t = map(int,stdin.readline().split())
    if n == 0 and t == 0:
        break
    for _ in range(t):
        a,op,b = stdin.readline().split()
        a,b = int(a),int(b)
        if op == "+":
            stdout.write(f"{(a + b) % n}\n")
        elif op == "-":
            stdout.write(f"{(a - b) % n}\n")
        elif op == "*":
            stdout.write(f"{(a * b) % n}\n")
        else:
            m = modInverse(b,n)
            stdout.write("-1\n") if m == -1 else stdout.write(f"{(a * m) % n}\n")
                
