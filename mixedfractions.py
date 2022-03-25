from sys import stdin,stdout

for line in stdin:
    a,b = map(int,line.split())
    if a == 0 and b == 0:
        break
    quotient = a//b; remainder = a - quotient*b
    stdout.write(f'{quotient} {remainder} / {b}\n')
