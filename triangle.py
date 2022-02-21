from sys import stdin,stdout
from math import floor,log10
# Perimeter of a Sierpinski triangle of order (n) is 3^(n+1)/2^n
def SierpinskiPerimeter(n):
    return (3**(n+1))/(2**n)

def numOfDigits(n):
    return 1 + floor(log10(n))

for linenum,line in enumerate(stdin):
    stdout.write(f"Case {linenum+1}: {numOfDigits(int(SierpinskiPerimeter(int(line))))}\n")

