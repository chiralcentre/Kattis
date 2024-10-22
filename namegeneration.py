from sys import stdin,stdout

consonants = "bcdfghjklmnpqrstvwxyz"
for i in range(int(stdin.readline())):
    string = []
    b = i + 63
    while b > 0:
        string.append(consonants[b % 21])
        b //= 21
        if len(string) % 3 == 2:
            string.append("a")
    stdout.write("".join(string))
    stdout.write("\n")
