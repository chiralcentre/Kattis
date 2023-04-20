from sys import stdin,stdout

def sum_square(n):
    t = 0
    while n > 0:
        d = n % 10
        t += d * d
        n //= 10
    return t

def check_happy(n):
    seen = set()
    while n > 9:
        n = sum_square(n)
        if n in seen:
            return 0
        seen.add(n)
    return 1 if n == 1 or n == 7 else 0

happy = [0 for _ in range(1000001)]
for i in range(1,1000001):
    happy[i] += happy[i - 1] + check_happy(i)

for _ in range(int(stdin.readline())):
    A,B = map(int,stdin.readline().split())
    stdout.write(f"{happy[B] - happy[A - 1]}\n")
