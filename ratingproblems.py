n,k = map(int,input().split())
scores = [int(input()) for _ in range(k)]
# minimum occurs when judges give -3 and maximum occurs when judges give 3
minimum,maximum = (sum(scores) + (n-k)*(-3))/n, (sum(scores) + (n-k)*(3))/n
print(f'{minimum} {maximum}')
