from sys import stdin,stdout

def solve(n):
    counter = 0
    while n > 0:
        n -= 7
        counter += 1
        if not n%10:
            return str(counter)
    return str(counter) if n >= 0 else "-1"

for _ in range(int(stdin.readline())):
    stdout.write(f"{solve(int(stdin.readline()))}\n")
