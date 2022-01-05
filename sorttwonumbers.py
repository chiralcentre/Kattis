print((lambda x: f'{x[0]} {x[1]}' if int(x[1]) > int(x[0]) else f'{x[1]} {x[0]}')(input().split()))
