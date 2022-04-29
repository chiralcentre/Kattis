from sys import stdin,stdout
from decimal import *
#Assume A has n digits and starts with digit B
#Let the new number after moving first digit to end of number be A'
#A' = (A - (10**(n-1))(B))(10) + B
#A' = AX
#AX = 10A - (10**n-1)B
#A = ((10**n - 1)/(10 - X))(B)
#Since A has < 10**8, max number of digits is 8
#Iterate through the number of digits(2 to 8) and all starting digits B (1 to 9)
# check if A obtained from formula is a valid solution

def moveFirstDigit(num):
    string = str(num)
    f = int(string[0]); n = len(string)
    return (num - (10**(n-1))*f)*10 + f

def possibleNum(d,b,X):
    return b*(10**d - 1)/Decimal(str(10-X)) #decimal object is used for precision

X = Decimal(stdin.readline())
numbers = []
if X == 10:
    stdout.write("No solution") # cannot divide by zero
else:
    for d in range(1,9):
        for b in range(1,10):
            a = possibleNum(d,b,X)
            if a%1 == 0: #integer:
                a = int(a)
                if a*X == moveFirstDigit(a):
                    numbers.append(a)
    stdout.write('\n'.join(str(a) for a in numbers)) if numbers else stdout.write("No solution")
