from sys import stdin,stdout
from math import sqrt

def curvespeed(R,S):
    return round(sqrt((R*(S+0.16))/0.067))

for line in stdin:
    R,S = line.split()
    R = int(R); S = float(S)
    stdout.write(str(curvespeed(R,S))+'\n')
