from sys import stdin,stdout

#perform recursive DFS from index 0
def DFS(n):
    if n == len(W): #end of word
        return 1
    if visited[n] != -1: #visited before
        return visited[n]
    string,total = "",0
    for i in range(n,len(W)):
        string += W[i]
        if string in dct:
            total = (total + dct[string]*DFS(i+1))%(10**9+7)
    visited[n] = total
    return total

#longest word is 32 characters long
#visited[n] keeps track of number of possible meanings at index position n
visited = [-1 for _ in range(33)] 
N,W = stdin.readline().split()
N = int(N); dct = {}
for i in range(N):
    word,value = stdin.readline().split()
    dct[word] = int(value) #dictionary words are distinct
stdout.write(str(DFS(0)))
