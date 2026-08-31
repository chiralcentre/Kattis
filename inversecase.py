from sys import stdin,stdout

line = stdin.readline().strip("\n")
for char in line:
    if char.islower():
        stdout.write(char.upper())
    else:
        stdout.write(char.lower())
