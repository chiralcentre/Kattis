from math import pi

M,N,R = input().split()
M,N,R = int(M),int(N),float(R)
ax,ay,bx,by = map(int,input().split())
print(min(abs(ay - by) / N * R + (min(ay,by) / N * R) * pi * abs(bx - ax) / M, (ay + by) / N * R))
