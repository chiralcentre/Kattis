from math import sqrt,ceil

#for any x between 1 to 99 inclusive, it takes no more than 9 times to curve before f^k(x) > 99
def solve(x,ylow,yhigh):
    lowest,highest = -1,-1
    for i in range(10):
        if ylow <= ceil(x) <= yhigh:
            if lowest == -1:
                lowest = i
            highest = i
        x = 10*sqrt(x)
    if lowest == -1:
        return "impossible"
    if yhigh == 100:
        highest = 10**9
    return f"{lowest} {highest}" if highest != 10**9 else f"{lowest} inf"
    
x,ylow,yhigh = map(int,input().split())
print(solve(x,ylow,yhigh))
