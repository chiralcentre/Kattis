from sys import stdin,stdout

while True:
    n = int(stdin.readline())
    if n == -1:
        break
    weak_vertices,neighbours = [],[set() for _ in range(n)]
    adjacency_matrix = [list(map(int,stdin.readline().split())) for _ in range(n)]
    # due to symmetric nature of adjacency matrix, only need to consider entries below or above diagonal
    for i in range(n):
        for j in range(i):
            if adjacency_matrix[i][j] == 1: #taking bottom half
                neighbours[i].add(j)
                neighbours[j].add(i)
    for k in range(n):
        weak = True
        for connection in neighbours[k]:
            other_neighbours = {x for x in neighbours[k] if x != connection}
            if len(neighbours[connection].intersection(other_neighbours)) > 0: # have at least two different neighbours that are direct neighbours of each other
                weak = False    
                break
        if weak:
            weak_vertices.append(str(k))
    stdout.write(' '.join(weak_vertices)+'\n')
    
                
