from sys import stdin,stdout

S = stdin.readline().strip()
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
for letter in S:
    if letter.lower() in vowels:
        stdout.write(letter)
