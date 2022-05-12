from random import randint
from sys import exit

print(randint(1,2)) #start with either 1 or 2
while True:
    x = int(input())
    if x%3: #not a multiple of 3
        print(x+3-x%3) #this guarantees a multiple of 3, since 3 - x%3 is either 1 or 2 if x is not a multiple of 3
        if x+3-x%3 == 99:
            exit(0)
    else: #multiple of 3
        print(x+randint(1,2))
