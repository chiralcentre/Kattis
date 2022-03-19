from sys import stdin,stdout

def gcd(e,f):
    while f > 0:
      rem = e%f
      e = f
      f = rem
    return e  
 
N = int(stdin.readline())
rings = list(map(int,stdin.readline().split()))
for i in range(1,N):
    HCF = gcd(rings[0],rings[i])
    stdout.write(f'{rings[0]//HCF}/{rings[i]//HCF}\n')
