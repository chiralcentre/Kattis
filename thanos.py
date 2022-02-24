from sys import stdin,stdout
from math import log10,floor

for _ in range(int(stdin.readline())):
    P,R,F = map(int,stdin.readline().split())
    stdout.write(str(floor(log10(F/P)/log10(R))+1)+'\n') if P <= F else stdout.write('0\n')
