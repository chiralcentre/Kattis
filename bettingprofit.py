from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    m,o,sign = stdin.readline().split()
    m,o = int(m),int(o)
    if sign == "+":
        stdout.write(f"{m / 100 * o}\n")
    else:
        stdout.write(f"{m / o * 100}\n")
