from sys import stdin,stdout

n = int(stdin.readline())
freq,prices = {},{}
for _ in range(n):
    x,y = stdin.readline().split()
    y = y.split(".")
    p = int(y[0]) * 100 + int(y[1])
    prices[x] = p # assume the price of a single item doesn't change
    freq[x] = freq.get(x,0) + 1
lst = sorted(prices.items(),key = lambda x: (x[1],x[0]))
for x,_ in lst:
    stdout.write(f"{x} {freq[x]}\n")
