from math import sqrt,pi,e,log
from sys import stdin,stdout
# logarithm must be used to prevent overflow error
for line in stdin:
    n = int(line)
    if n == 0:
        break
    # break down logarithm of factorial as sum
    base = sum(log(i) for i in range(2,n+1)) - 0.5*log(2*n*pi) - n*log(n) + n 
    stdout.write(f'{e**base}\n')
    
