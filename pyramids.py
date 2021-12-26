N = int(input())

n,counter,bricks = 1,0,0

while bricks + n**2 <= N:
    bricks += n**2
    n += 2
    counter += 1

print(counter)
