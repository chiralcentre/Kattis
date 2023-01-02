from sys import stdin

A,B = map(int,stdin.readline().split())
rem = A % B
print(min(rem,B - rem))

