from sys import stdin,stdout

s = int(stdin.readline())
points = set()
while len(points) < 4:
    s += s // 13 + 15
    d = s % 100
    points.add((d // 10, d % 10))

moves = 0
while points:
    L = int(stdin.readline())
    x2,y2 = L // 10, L % 10
    if (x2,y2) in points:
        stdout.write("You hit a wumpus!\n")
        points.remove((x2,y2))
    if points:
        lowest = 100000000
        for x,y in points:
            lowest = min(lowest, abs(x - x2) + abs(y - y2))
        stdout.write(f"{lowest}\n")
    moves += 1
stdout.write(f"Your score is {moves} moves.\n")
