from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    string = stdin.readline().strip("\n")
    n = len(string)
    for i in range(n):
        s = string[:i + 1]
        d = n // (i + 1)
        res = s * (d + 1)
        if res.startswith(string):
            stdout.write(f"{i + 1}\n")
            break
