from math import factorial
#hat matching problem: find probability of at least one person getting back his own hat
print((lambda N: sum(pow(-1, r - 1) / factorial(r) for r in range(1,min(N + 1,10))))(int(input()))) #number < 10^-6 on 10th iteration
