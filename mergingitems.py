from sys import stdin

freq = {}
for _ in range(int(stdin.readline())):
    v = int(stdin.readline())
    freq[v] = freq.get(v,0) + 1
n = int(stdin.readline())
freq[0] = freq.get(0,0) + 3 * n
# at no point during the round will there be more than one item of value 10
# iterate from 0 to 10
for i in range(11):
    f = freq.get(i,0)
    if f >= 2: # merge if there is more than 2
        L = f // 2
        f -= L * 2
        if f > 0:
            freq[i] = f
        else:
            freq.pop(i)
        freq[i + 1] = freq.get(i + 1,0) + L
output = []
for i in range(11):
    f = freq.get(i,0)
    if f > 0:
        for _ in range(f):
            output.append(str(i))
print(" ".join(output))
