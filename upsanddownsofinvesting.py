from sys import stdin,stdout

#overall approach runs in #O(s)
s,n,m = map(int,stdin.readline().split())
prices = []
while len(prices) < s:
    prices.extend(list(map(int,stdin.readline().split())))
#let 1 denote increasing, 0 denote decreasing
trends = []
prev,t,counter = prices[0],1,0
#note no two consecutive stock prices are the same
for i in range(1,s):
    new_t = 1 if prices[i] > prev else 0
    if new_t == t:
        counter += 1
    else:
        trends.append((t,counter))
        counter = 1
        t = new_t
    prev = prices[i]
trends.append((t,counter))
peaks,valleys = 0,0
for i in range(len(trends) - 1):
    t1,d1 = trends[i]
    t2,d2 = trends[i + 1]
    #+1 offset is to include the stock price at the peak/valley itself
    if t1 == 1 and t2 == 0 and d1 + 1 >= n and d2 + 1 >= n:
        peaks += 1
    elif t1 == 0 and t2 == 1 and d1 + 1 >= m and d2 + 1 >= m:
        valleys += 1
stdout.write(f"{peaks} {valleys}\n")
