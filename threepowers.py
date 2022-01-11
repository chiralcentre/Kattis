from math import log2
def threepowers(n):
    s = []
    if n == 1:
        return s
    else:
        highest_power = int(log2(n-1))
        while n > 1:
            n -= 2**(highest_power) 
            s = [3**highest_power] + s
            if n > 1:
                highest_power = int(log2(n-1))
        return s
                
while True:
    n = int(input())
    if n == 0:
        break
    print('{ ' + ', '.join(map(str,threepowers(n))) + ' }')
