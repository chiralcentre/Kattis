from math import log2,sqrt

#maximum factorial given value of m is 12
factorial = [1]
for i in range(1,13):
    factorial.append(factorial[-1]*i)
EPSILON = 10**-6
def verdict(m,n,t):
    if t == 1:
        return "AC" if n <= 12 and factorial[n] <= m else "TLE"
    elif t == 2:
        base = log2(m)
    elif t == 3:
        base = m**(1/4)
    elif t == 4:
        base = m**(1/3)
    elif t == 5:
        base = sqrt(m)
    elif t == 6:
        return "AC" if n*log2(n) <= m + EPSILON else "TLE"
    else:
        base = m
    return "AC" if n <= base + EPSILON else "TLE"    
        
m,n,t = map(int,input().split())
print(verdict(m,n,t))
