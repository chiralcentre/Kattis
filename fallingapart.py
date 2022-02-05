n = int(input())
pieces = sorted(list(map(int,input().split())))
A,B,turn = 0,0,True #True is Alice's turn, False is Bob's turn
# every player chooses the highest piece
while pieces:
    if turn:
        A += pieces.pop()
    else:
        B += pieces.pop()
    turn = False if turn else True
print(f'{A} {B}')
