from sys import stdin,stdout

def get_unlikeliness(s1,s2):
    nounter = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            nounter += 1
    return nounter

n,k = map(int,stdin.readline().split())
INF = 10**9 # use one billion to represent infinity
#Prim's variant for dense graphs is used in O(n^2) time
strings = [stdin.readline().strip() for _ in range(n)]
A,taken = [(INF,v) for v in range(n)],[False for _ in range(n)]
A[0] = (0,0) #start from first point
taken[0] = True; cost = 0; counter = 1; answer = []
while counter < n: #O(n)
    lowest,v = INF,0 # scan A to get v where A[v][0] is minimum in A
    for i in range(n): #O(n)
        if A[i][0] < lowest:
            lowest = A[i][0]
            v = i
    #add vertices to taken
    if not taken[v]:
        taken[v] = True
        counter += 1
        answer.append(f"{v} {A[v][1]}")
    if not taken[A[v][1]]:
        taken[A[v][1]] = True
        counter += 1
    cost += A[v][0]
    A[v] = (INF,A[v][1]) #prevent picking the same point
    for j in range(n): #O(n)
        if not taken[j] and A[j][0] > get_unlikeliness(strings[j],strings[v]):
            A[j] = (get_unlikeliness(strings[j],strings[v]),v)
stdout.write(f"{cost}\n")
stdout.write('\n'.join(answer))

