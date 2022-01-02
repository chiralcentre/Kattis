from math import pi

while True:
    testcase = input().split()
    r,m,c = float(testcase[0]),int(testcase[1]),int(testcase[2])
    if r == m == c == 0:
        break
    actual_area,estimate = pi*r**2,(c/m)*(2*r)**2
    print(f'{actual_area} {estimate}')
