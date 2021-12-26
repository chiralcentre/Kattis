import sys

for line in sys.stdin:
    inpt = line.split()
    print(abs(int(inpt[0]) - int(inpt[1])))
