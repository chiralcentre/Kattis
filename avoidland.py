from sys import stdin,stdout

#since there are n pawns, every single row and column must be taken.
#overall time complexity is O(n log n)
n = int(stdin.readline())
x_coords,y_coords = [],[]
for i in range(n):
    x,y = map(int,stdin.readline().split())
    x_coords.append(x); y_coords.append(y)
x_coords.sort(); y_coords.sort()
stdout.write(str(sum(abs(i + 1 - x_coords[i]) + abs(i + 1 - y_coords[i]) for i in range(n))))
