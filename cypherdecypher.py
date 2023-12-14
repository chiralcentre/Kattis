from sys import stdin,stdout

MKIA = list(map(int,list(stdin.readline().strip())))
for i in range(int(stdin.readline())):
    string = stdin.readline().strip()
    for j in range(len(string)):
        stdout.write(chr((((ord(string[j]) - 65) % 26) * MKIA[j]) % 26 + 65))
    stdout.write("\n")
