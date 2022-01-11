n = int(input())
prices = sorted(list(map(int,input().split())))
# the cheapest item per triplet is discounted, and if the group of items is not a triplet, there is no discount
discount = sum(prices[i] for i in range(n%3,n,3))
print(discount)
