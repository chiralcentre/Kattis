from math import sqrt

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if not n%2:
        return False
    for i in range(3,int(sqrt(n))+1,2): #n must be odd now
        if not n%i:
            return False
    return True


counter,n = 0,1
while counter < 100:
    n += 1
    while not isPrime(n):
        n += 1
    print(n)
    counter += 1
