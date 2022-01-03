values = {'A': [11,11],
          'K': [4,4],
          'Q': [3,3],
          'J': [20,2],
          'T': [10,10],
          '9': [14,0],
          '8': [0,0],
          '7': [0,0]}

first_line = input().split()
N,B = int(first_line[0]),first_line[1]
cards = [input().strip() for _ in range(4*N)]

points = 0
for card in cards:
    points += values[card[0]][0] if card[1] == B else values[card[0]][1]
    
print(points)
