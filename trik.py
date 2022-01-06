ball = ['B',0,0]
moves = input().strip()
for move in moves:
    if move == 'A':
        ball[0],ball[1] = ball[1],ball[0]
    elif move == 'B':
        ball[1],ball[2] = ball[2],ball[1]
    else:
        ball[0],ball[2] = ball[2],ball[0]
print(ball.index('B')+1)
