from sys import stdin,stdout

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
neg,pos = [],[]
for n in nums:
    if n > 0: #positive number
        while neg and n > 0:
            n += neg.pop()
        if n > 0:
            pos.append(n)
        elif n < 0:
            neg.append(n)
    else: #negative number
        while pos and n < 0:
            n += pos.pop()
        if n > 0:
            pos.append(n)
        elif n < 0:
            neg.append(n)
if len(pos) > len(neg):
    stdout.write("Positives win!\n")
    stdout.write(" ".join(str(num) for num in pos))
elif len(pos) == len(neg):
    stdout.write("Tie!\n")
else:
    stdout.write("Negatives win!\n")
    stdout.write(" ".join(str(num) for num in neg))
        
