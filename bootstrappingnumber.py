from math import log

def f(x):
    return x**x

def derivative(x):
    return (log(x)+1)*x**x

n = int(input())
x0 = 1
while f(x0) < n: #maximum x0 = 10 based on given input limits
    x0 += 1

counter = 0
while counter < 7: # 7 iterations of newton-raphson method is the minimum by trial and error
    x0 = x0 - (f(x0)-n)/derivative(x0)
    counter += 1
print(x0)
