from sys import stdin,stdout
from math import ceil

for _ in range(int(stdin.readline())):
    stdout.write(f'{ceil(int(stdin.readline())/400)}\n')
