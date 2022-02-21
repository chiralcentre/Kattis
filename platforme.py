from sys import stdin,stdout
# input is small so time complexity does not matter
N = int(stdin.readline())
platforms = []
for _ in range(N): #O(N)
    y,x1,x2 = map(int,stdin.readline().split())
    platforms.append((y,x1,x2))
#O(N log N)
platforms = sorted(platforms,key = lambda x:x[0]) #sort by height in ascending order
total = 0
while len(platforms) > 1: #O(N^2) 
    h1,x1,x2 = platforms.pop()
    end = len(platforms)-1 #reference to last element in platforms
    left,right = False,False #left and right boolean variables track if left and right pillar have been found
    while (not left or not right) and end >= 0: #go down platforms from tallest possible
        h2,x3,x4 = platforms[end]
        if x3 <= x1 < x4 and not left:
            left = True
            total += h1 - h2
        if x3 < x2 <= x4 and not right:
            right = True
            total += h1 - h2
        end -= 1
    if not left and not right:
        total += h1*2
    elif not left or not right:
        total += h1
#include pillars of lowest platform
stdout.write(str(total+platforms[0][0]*2))       

