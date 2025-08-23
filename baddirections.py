from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    k,n = stdin.readline().split()
    k = int(k)
    for c in n:
        stdout.write(f"{(int(c) + k) % 10}")
    stdout.write("\n")
