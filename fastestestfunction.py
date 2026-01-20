x,y = map(lambda x: float(x) / 100,input().split())
print(x / y * (1 - y) / (1 - x))
