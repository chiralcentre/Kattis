from sys import stdin,stdout

n = int(stdin.readline())
# top half
for i in range(1 + n):
    stdout.write(" ")
stdout.write("x\n")
for i in range(n):
    for j in range(n - i):
        stdout.write(" ")
    stdout.write("/")
    for k in range(1 + (i << 1)):
        stdout.write(" ")
    stdout.write("\\\n")
# middle
stdout.write("x" + " " * (1 + (n << 1)) + "x\n")
# lower half
for i in range(n):
    for j in range(i + 1):
        stdout.write(" ")
    stdout.write("\\")
    for k in range(1 + ((n - i - 1) << 1)):
        stdout.write(" ")
    stdout.write("/\n")
for i in range(1 + n):
    stdout.write(" ")
stdout.write("x\n")
