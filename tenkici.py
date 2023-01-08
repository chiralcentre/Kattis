from sys import stdin,stdout

N = int(stdin.readline())
x_coords,y_coords = [],[]
for i in range(N):
    x,y = map(int,stdin.readline().split())
    x_coords.append((x,i+1))
    y_coords.append((y,i+1))
#sort by row and col
x_coords.sort(); y_coords.sort()
ans = []
#assign first tank to first row and so on
#assign tanks that need to move up in top down order
#assign tanks that need to move down in bottom up order
for i in range(N):
    x,j = x_coords[i]
    while x > i + 1:
        x -= 1
        ans.append(f"{j} U")
for i in range(N - 1,-1,-1):
    x,j = x_coords[i]
    while x < i + 1:
        x += 1
        ans.append(f"{j} D")
#sort by column
#assign first tank to first col and so on
#assign tanks that need to move left in left to right order
#assign tanks that need to move right in right to left order
for i in range(N):
    y,j = y_coords[i]
    while y > i + 1:
        y -= 1
        ans.append(f"{j} L")
for i in range(N - 1,-1,-1):
    y,j = y_coords[i]
    while y < i + 1:
        y += 1
        ans.append(f"{j} R")
stdout.write(f"{len(ans)}\n")
stdout.write("\n".join(row for row in ans))
stdout.write("\n")

