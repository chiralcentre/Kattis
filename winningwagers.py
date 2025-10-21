from sys import stdin

N = int(stdin.readline())
events = stdin.readline().split()
L = int(stdin.readline())
# numerator and denominator of fraction representing winning probability
denominator = 1
for e in events:
    if e == "COIN":
        denominator *= 2
    elif e == "DIE":
        denominator *= 6
    else:
        denominator *= 52
losing_numerator = denominator - 1
print(L * losing_numerator)
