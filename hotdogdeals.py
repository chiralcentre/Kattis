# deal 1: 1 hot dog + 1 soda for 499 ISK
# deal 2: 2 hot dogs + 1 soda for 549 ISK
# while n >= 2, greedily take deal 2 (even if there is excess soda left)
# if n == 1, choose deal 1 only if there is one soda left, else buy hotdog alone

n,m = map(int,input().split())
cost = 0
# let d = number of deal 2 taken
d = n // 2
cost += d * 549
n -= d * 2
m -= d
if n == 1:
    if m > 0:
        m -= 1
        cost += 499
    else:
        cost += 299
    n -= 1
if m > 0:
    cost += m * 249
print(cost)
