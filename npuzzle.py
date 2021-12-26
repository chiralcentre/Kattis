layout = [['A','B','C','D'],
         ['E','F','G','H'],
         ['I','J','K','L'],
         ['M','N','O','.']]

def buildpuzzle(lst):
    dict1 = {}
    for i in range(4):
        for j in range(4):
            dict1[lst[i][j]] = (i,j)
    return dict1

board = [list(input().strip()) for i in range(4)]
ideal_positions,positions = buildpuzzle(layout),buildpuzzle(board)
        
distance = 0
for key in ideal_positions:
    if key != '.':
        distance += abs(ideal_positions[key][0] - positions[key][0]) + abs(ideal_positions[key][1] - positions[key][1])
print(distance)
