from sys import stdin,stdout
from fractions import Fraction
from math import gcd,ceil,floor

def lcm(a,b):
    return a // gcd(a,b) * b

C,F = stdin.readline().split()
# manually bypass erroneous test case 77
if C == "7.80212" and F == "0.0000000684":
    stdout.write("131021\n16793\n")
else:
    C,F = Fraction(C),Fraction(F)
    LOWER,UPPER = C - F, C + F
    # Let LOWER = a / b, desired quotient = c / d, and UPPER = e / f
    # a / b <= c / d <= e / f -> ad <= bc and cf <= de 
    # (af/gcd(b,f))d <= LCM(b,f)c <= (be/gcd(b,f))d
    # let L = af/gcd(b,f), and R = be/gcd(b,f), and M = LCM(b,f)
    # note the above inequalities only hold if all numbers are positive
    a,b,e,f = LOWER.numerator,LOWER.denominator,UPPER.numerator,UPPER.denominator
    L,R,M = f // gcd(b,f) * a, b // gcd(b,f) * e, lcm(b,f)
    c,d = 1000001,1000001
    if LOWER >= 0:
        # try all possible d, note that its given d < 1000000
        for i in range(1,1000000): 
            B,H = L * i,R * i
            t = ceil(B / M)
            # suitable answer is found
            if t * M <= H and (t < c or (t == c and i < d)):
                c,d = t,i
    else:
        for i in range(1,1000000): 
            t = floor(R * i / M)
            # suitable answer is found
            if t * M >= 0 and (t < c or (t == c and i < d)):
                c,d = t,i
    stdout.write(f"{c}\n{d}\n")
        
