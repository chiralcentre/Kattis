from sys import stdin,stdout

N = int(stdin.readline())
tea_prices = list(map(int,stdin.readline().split()))
M = int(stdin.readline())
top_prices = list(map(int,stdin.readline().split()))
lowest = 10**9
for i in range(N):
    K,*toppings = map(lambda x: int(x) - 1,stdin.readline().split())
    for t in toppings:
        if tea_prices[i] + top_prices[t] < lowest:
            lowest = tea_prices[i] + top_prices[t]
X = int(stdin.readline())
stdout.write(f"{max(X//lowest - 1,0)}\n")
