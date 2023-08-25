s,n = map(int,input().split())
players = [(i+1,'FOLDED') for i in range(n)]
start = 0 # starts from first player
# time complexity does not matter due to small s and n
# repeat until one hand is left
while len(players) > 1:
    start = (start+s-1)%len(players)
    player,hand_state = players[start]
    if hand_state == 'FOLDED': # replace with two copies of fist
        players[start] = (player,'FIST')
        players.insert(start,(player,'FIST'))
    elif hand_state == 'FIST':
        players[start] = (player,'PALM')
        start = (start+1)%len(players)
    elif hand_state == 'PALM':
        players.pop(start)
        
print(players[0][0])
