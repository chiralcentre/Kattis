from sys import stdin,stdout

#O(N)
def solve(N,degrees):
    for i in range(1,N):
        possible = False
        for j in range(i): #shortest path must be from smallest to largest index
            if degrees[j] > 0:
                degrees[i] -= 1 
                degrees[j] -= 1
                possible = True
                break
        if not possible:
            return "NO"
    #graph is not a tree if max(degrees) > 0 after processing
    return "NO" if max(degrees) > 0 else "YES"
    
N = int(stdin.readline())
degrees = list(map(int,stdin.readline().split()))
stdout.write(solve(N,degrees))
