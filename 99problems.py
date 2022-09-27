N = int(input())
if N < 100:
    print(99)
else:
    multiple = N//100
    lower = (multiple-1)*100+99
    upper = multiple*100+99
    print(lower) if N - lower < upper - N else print(upper)
