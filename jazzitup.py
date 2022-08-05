#To find m: find a number relatively prime to n
#this can be done by iterating through the first few primes starting from 2
#This is fast since you’ll allways find a solution among the first 7 primes.
#Proof: 2*3*5*7*11*13*17 = 510510 > 100000
n = int(input())
for f in [2,3,5,7,11,13,17]:
    if n%f:
        print(f)
        break
