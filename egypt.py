import sys

def right_triangle(lst):
    if lst[0]**2 + lst[1]**2 == lst[2]**2:
        return('right')
    else:
        return('wrong')
    
for line in sys.stdin: 
    inpt = sorted(list(map(int, line.split())))
    if 0 in inpt:
        pass
    else:
        print(right_triangle(inpt))


