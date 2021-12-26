from math import ceil,log2

def printer(num):
    return ceil(log2(num)) + 1

print(printer(int(input())))
    
