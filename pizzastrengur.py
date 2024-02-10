from sys import stdin
from random import shuffle

# expected number of tries to get one letter right is (1 + 2 + 3 + 3) / 4 = 2.25
n = int(stdin.readline())
prefix,response,letters = "",0,["P", "I", "Z", "A"]
for i in range(n):
    shuffle(letters)
    for j in range(3):
        print(prefix + letters[j], flush = True)
        response = int(stdin.readline())
        if response != 0:
            prefix += letters[j]
            break
    else: # last letter is part of prefix
        prefix += letters[3]
if response != 2:
    print(prefix, flush = True)
