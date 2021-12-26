from math import factorial

def catalan(q):
    return factorial(2*q)//(factorial(q+1)*factorial(q))

n = int(input())
counter = 0

while counter < n:
    num = int(input())
    print(catalan(num))
    counter += 1
