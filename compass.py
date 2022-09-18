n1,n2 = int(input()),int(input())
clockwise = (360 + n2 - n1)%360
anticlockwise = abs(n2-n1) - 360 if n2 > n1 else n2 - n1
print(anticlockwise) if abs(anticlockwise) < abs(clockwise) else print(clockwise)
