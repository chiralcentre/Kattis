from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    i = int(stdin.readline())
    i += 1
    # get number of digits
    # do it this way instead of using log to avoid floating point imprecision
    d = 0
    while pow(2,d) < i:
        d += 1
    if pow(2,d) > i:
        d -= 1
    gap = bin(i - pow(2, d)).replace("0b","")
    stdout.write(f"{gap.rjust(d, '0')}\n")
