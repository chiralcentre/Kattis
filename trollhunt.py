from math import ceil
b,k,g = map(int,input().split())
# groups = k//g, number of bridges to explore b - 1
print(ceil((b-1)/(k//g)))
