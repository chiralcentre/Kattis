from math import sqrt,ceil
n = int(input())

def prime(num):
    factors = []
    while num > 1:
        for i in range(2,ceil(sqrt(num))+1): #do prime factorisation in ascending order
            if not num%i:
                num //= i
                factors.append(i)
                break
            if i > sqrt(num): #num is prime
                factors.append(num)
                return factors
    return factors

print(len(prime(n)))
