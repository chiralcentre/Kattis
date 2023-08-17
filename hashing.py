from sys import stdin,stdout

# use large M to prevent collisions
MAX_N = 300001
p,M = 131,pow(10,18) + 9
P,h = [0 for i in range(MAX_N)],[0 for i in range(MAX_N)]

def computeRollingHash(T):
    P[0] = 1
    for i in range(1,len(T)):
        P[i] = (P[i-1] * p) % M
    h[0] = 0
    for i in range(len(T)):
        if i != 0:
            h[i] = h[i-1]
        h[i] = (h[i] + (ord(T[i]) * P[i]) % M) % M

def extEuclid(a, b):
  xx, yy = 0, 1
  x, y = 1, 0
  while b != 0:
    q = a // b
    a, b = b, a % b
    x, xx = xx, x - q * xx
    y, yy = yy, y - q * yy
  return a, x, y

def modInverse(b, m):
  d, x, y = extEuclid(b, m)
  if d != 1:
    return -1
  return (x + m) % m

def hash_fast(L, R):
  if L == 0:
    return h[R]
  ans = ((h[R] - h[L-1]) % M + M) % M
  ans = (ans * modInverse(P[L], M)) % M
  return ans

S = stdin.readline().strip()
computeRollingHash(S)
for i in range(int(stdin.readline())):
    L,R = map(int,stdin.readline().split())
    stdout.write(f"{hash_fast(L,R - 1)}\n")
