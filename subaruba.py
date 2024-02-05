from sys import stdin,stdout

VOWELS = {'A', 'E', 'I', 'O', 'U', 'Y'}

first = stdin.readline().strip()
n = int(stdin.readline())
if first == "A":
    for i in range(n):
        line = stdin.readline().strip()
        j = 0
        while j < len(line):
            upper,found = False,False
            if line[j].lower() == "u" and j + 1 < len(line) and line[j + 1] == "b":
                upper,found = line[j].isupper(),True
                j += 2
            stdout.write(line[j].upper()) if found and upper else stdout.write(line[j])
            j += 1
        stdout.write("\n")
else:
    for i in range(n):
        line = stdin.readline().strip()
        j = 0
        while j < len(line):
            if line[j].upper() in VOWELS:
                stdout.write("Ub") if line[j].isupper() else stdout.write("ub")
            stdout.write(line[j])
            j += 1
        stdout.write("\n")
