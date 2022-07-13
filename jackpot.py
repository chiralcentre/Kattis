from sys import stdin,stdout
from math import gcd

def compute_lcm(a,b):
    return a*b//gcd(a,b)

def process():
    w = int(stdin.readline())
    wheels = list(map(int,stdin.readline().split()))
    if w == 1:
        return f"{wheels[0]}\n" if wheels[0] <= BILLION else "More than a billion.\n"
    else:
        a = wheels[0]
        for i in range(w-1):
            a = compute_lcm(a,wheels[i+1])
            if a > BILLION:
                return "More than a billion.\n"
        return f"{a}\n"
                
BILLION = 1000000000
for _ in range(int(stdin.readline())):
   stdout.write(process())
                
        
        
