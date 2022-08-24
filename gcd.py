def gcd(e,f):
    while f > 0:
      rem = e%f
      e = f
      f = rem
    return e  

A,B = map(int,input().split())
print(gcd(A,B))
