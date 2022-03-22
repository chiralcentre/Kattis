from sys import stdin,stdout
from collections import deque

N,H,L = map(int,stdin.readline().split())
horror_list = set(map(int,stdin.readline().split()))
adjacency_list = [[] for _ in range(N)]
for i in range(L): #O(L)
    a,b = map(int,stdin.readline().split())
    adjacency_list[a].append(b)
    adjacency_list[b].append(a)
#left attribute represents cost
frontier,visited = deque([]),[False for _ in range(N)]
# counter keeps track of number of visited vertices
largest_HI,best_movie,counter = -1,-1,len(horror_list)
for num in horror_list: #O(H)
    frontier.append((0,num))
    visited[num] = True
    
while frontier: #BFS - O(H + L)
    horror_index,movie = frontier.popleft()
    if horror_index > largest_HI or (horror_index == largest_HI and movie < best_movie):
        largest_HI,best_movie = horror_index,movie
    for neighbour in adjacency_list[movie]:
        if not visited[neighbour]:
            visited[neighbour] = True
            frontier.append((horror_index+1,neighbour))
            counter += 1
#all movies are connected to horror list movies            
if counter == N:
    stdout.write(f'{best_movie}\n')
else: # there are movies not connected to horror list movies
    stdout.write(f'{visited.index(False)}\n') #O(H) - returns lowest index of movie not connected to horror list movies
    
    
        
        
        
