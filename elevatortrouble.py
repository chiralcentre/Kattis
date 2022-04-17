from collections import deque

def BFS(f,s,g,u,d):
    if s == g:
        return '0'
    s -= 1; g -=1  #offset by 1 due to zero indexing
    visited,frontier = [False for _  in range(f)],deque([(s,0)]) #right attribute keeps track of number of pushes
    visited[s] = 0
    while frontier: #BFS from source
        start,counter = frontier.popleft()
        a = start + u if start + u <= f - 1 else start
        b = start - d if start - d >= 0 else start
        if a == g or b == g:
            return str(counter+1)
        if not visited[a]:
            visited[a] = True
            frontier.append((a,counter+1))
        if not visited[b]:
            visited[b] = True
            frontier.append((b,counter+1))
    return "use the stairs" #not possible

f,s,g,u,d = map(int,input().split())
print(BFS(f,s,g,u,d))
