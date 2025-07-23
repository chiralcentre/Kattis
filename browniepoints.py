from sys import stdin,stdout

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    points = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
    a,b = points[n // 2]
    stan_score,ollie_score = 0,0
    for x,y in points:
        if x != a and y != b: # uncrossed brownie point
            if (x > a and y > b) or (x < a and y < b): # top right and bottom left quadrant
                stan_score += 1
            else:
                ollie_score += 1
    stdout.write(f"{stan_score} {ollie_score}\n")
