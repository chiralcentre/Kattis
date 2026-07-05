from sys import stdin,stdout

s = stdin.readline().strip()
vowels = {"a","e","i","o","u"}
vowels_sub = []
for char in s:
    if char.lower() in vowels:
        vowels_sub.append(char)
for char in s:
    if char.lower() in vowels:
        stdout.write(vowels_sub.pop())
    else:
        stdout.write(char)
