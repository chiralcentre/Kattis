from math import log

def f(x,C):
    return x**x-C

def derivative(x):
    return (log(x)+1)*x**x

n = int(input())
x0 = 1
while f(x0,n) < 0: #maximum x0 = 10 based on given input limits
    x0 += 1

counter = 0
while counter < 7: # 7 iterations of newton-raphson method is sufficient 
    x0 = x0 - f(x0,n)/derivative(x0)
    counter += 1
print(x0)
