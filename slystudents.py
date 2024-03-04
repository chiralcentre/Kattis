from sys import stdin,stdout
from math import gcd

def convertToBase3(num):
    res = []
    while num > 0:
        rem = num % 3
        res.append(rem)
        num //= 3
    return "".join(str(res[i]) for i in range(len(res) - 1, -1, -1))

words = stdin.readline().split()
for w in words:
    codes = [ord(char) for char in w]
    HCF = codes[0]
    for i in range(1,len(codes)):
        HCF = gcd(HCF, codes[i])
    stdout.write(f"{HCF}\n")
    stdout.write(" ".join(convertToBase3(c // HCF) for c in codes))
    stdout.write("\n")
