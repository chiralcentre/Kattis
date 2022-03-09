from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n,m,l = map(int,stdin.readline().split())
    tiles,knocked_over = {num:[] for num in range(1,n+1)},set()
    for i in range(m):
        x,y = map(int,stdin.readline().split())
        tiles[x].append(y) #each tile can be pointing to numerous other tiles
    for j in range(l):
        frontier = [int(stdin.readline())] #DFS
        while frontier:
            z = frontier.pop()
            knocked_over.add(z)
            if z in tiles:
                while tiles[z]:
                    a = tiles[z].pop()
                    if a in tiles:
                        frontier.append(a)
                        knocked_over.add(a)
                tiles.pop(z)              
    stdout.write(f'{len(knocked_over)}\n')
