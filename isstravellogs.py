from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    freq = {}
    nums = stdin.readline().split()
    for num in nums:
        code = num[0] + num[-1]
        freq[code] = freq.get(code, 0) + 1
    stdout.write(" ".join(str(v) for k,v in sorted(freq.items())))
    stdout.write("\n")
