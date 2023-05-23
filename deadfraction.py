from math import gcd

#using stdin,stdout for this question will lead to a compile error for some reason
while True:
    line = input().strip()
    if line == "0":
        break
    z = line[2:-3]; L = len(z)
    num,denom = 10**9,10**9
    #try all possible sequences of repeating digits
    for i in range(L):
        r,o = z[i:],z[:i]
        r = int(r)
        o = 0 if not o else int(o)
        #a,b is the simplified numerator and denominator of the non repeating portion
        g1 = gcd(o,pow(10,i))
        a,b = o // g1, pow(10, i) // g1
        #c,d is the simplified numerator and denominator of the repeating portion
        g2 = gcd(r,pow(10, L))
        c,d = r // g2, pow(10, L) // g2
        #find sum of repeating portion using infinite GP formula
        #sum of infinite GP = s/(1 - R) where s is initial term and R is common ratio
        #note in this case, s = c/d, and 1 - R = r1 / r2
        #resulting fraction is e/f = (c * r2) / (d * r1)
        r1,r2 = pow(10,L - i) - 1, pow(10,L - i)
        g3 = gcd(c * r2, d * r1)
        e,f = (c * r2) // g3, (d * r1) // g3
        #add a/b to e/f to get (af + be)/bf
        g4 = gcd(a*f + b*e, b*f)
        g,h = (a*f + b*e) // g4, (b*f) // g4
        if h < denom:
            num,denom = g,h
    print(f"{num}/{denom}")
