import sys
from math import factorial

for line in sys.stdin:
    word = line.strip()
    length,unique_letters = len(word),{}
    for char in word:
        unique_letters[char] = 1 if char not in unique_letters else unique_letters[char]+1
    anagrams = factorial(length) 
    for value in unique_letters.values():
        anagrams //= factorial(value) #account for repetitions
    print(anagrams)

    
