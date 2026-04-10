PI = 3.14159265
w,h = map(int,input().split())
L = min(w,h)
r = L / 2
A = w * h
if 2 * r * r * PI >= A:
    print("circle")
elif L * L * 2 >= A:
    print("square")
else:
    print("blank")
    
