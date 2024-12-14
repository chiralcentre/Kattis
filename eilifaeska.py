from sys import stdin,stdout

# solve case by case
# when n = 1, desired result is always possible with 0 moves
# when n = 2, desired result is always possible with 1 move (pour from larger glass to smaller glass)
# when n = 3, desired result is only possible if there is a glass with volume a such that a is the average of the other two glasses
# when n = 4, desired result is possible in at most 4 moves
# WLOG, let a < b < c < d
# balance a and b to get two glasses with volume e, e = (a + b)/2
# balance c and d to get two glasses with volume f, f = (c + d)/2
# balance e and f in two moves for the two pairs of glasses
n = int(stdin.readline())
liquid = list(map(lambda x: int(x),stdin.readline().split()))
liquid_pairs = sorted([(liquid[i],i) for i in range(n)])
total = sum(liquid)
if n == 1:
    stdout.write("0\n")
elif n == 2:
    stdout.write("1\n")
    stdout.write(f"{liquid_pairs[-1][1] + 1} {liquid_pairs[0][1] + 1}\n")
elif n == 3:
    if liquid_pairs[1][0] * 3 != total:
        stdout.write("-1\n")
    else:
        stdout.write("1\n")
        stdout.write(f"{liquid_pairs[-1][1] + 1} {liquid_pairs[0][1] + 1}\n")
elif n == 4:      
    ops = []
    # pour from b to a if b > a
    if liquid_pairs[1][0] > liquid_pairs[0][0]:
        ops.append((liquid_pairs[1][1],liquid_pairs[0][1]))
        first,last = liquid_pairs[1][1],liquid_pairs[0][1]
        average = (liquid[first] + liquid[last]) / 2
        liquid[first] = average
        liquid[last] = average
        liquid_pairs = sorted([(liquid[i],i) for i in range(n)])
    # pour from d to c if d > c
    if liquid_pairs[3][0] > liquid_pairs[2][0]:
        ops.append((liquid_pairs[3][1],liquid_pairs[2][1]))
        first,last = liquid_pairs[3][1],liquid_pairs[2][1]
        average = (liquid[first] + liquid[last]) / 2
        liquid[first] = average
        liquid[last] = average
        liquid_pairs = sorted([(liquid[i],i) for i in range(n)])
    # pour from c to a, from d to b
    if liquid_pairs[2][0] > liquid_pairs[0][0]:
        ops.append((liquid_pairs[2][1],liquid_pairs[0][1]))
    if liquid_pairs[3][0] > liquid_pairs[1][0]:
        ops.append((liquid_pairs[3][1],liquid_pairs[1][1]))
    stdout.write(f"{len(ops)}\n")
    for u,v in ops:
        stdout.write(f"{u + 1} {v + 1}\n")

