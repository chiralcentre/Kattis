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

def happy(n):
    sequence = set()
    while True: # terminates if a repeat is encountered
        n = sum(int(digit)**2 for digit in str(n))
        if n == 1:
            return True
        if n in sequence:
            return False
        sequence.add(n)

for _ in range(int(input())):
    K,m = map(int,input().split())
    print(f'{K} {m} YES') if isPrime(m) and happy(m) else print(f'{K} {m} NO')
