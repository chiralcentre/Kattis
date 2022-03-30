from math import sqrt

coordinates = [(0,0) for _ in range(9)]
for i in range(3):
    line = input().split()
    for j in range(3):
        coordinates[int(line[j])-1] = (i,j) #offset by 1 due to zero indexing
distance = sum(sqrt((coordinates[j][0] - coordinates[j+1][0])**2 + (coordinates[j][1]-coordinates[j+1][1])**2) for j in range(8))
print(distance)
