from math import factorial
# for n = 20, e is accurate to more than 15 decimal places
print(sum(1/factorial(i) for i in range(min(int(input())+1,20)))) 
