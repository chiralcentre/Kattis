def possibletriangle(N,sticks):
    for i in range(0,N-2):
        # triangle inequality with equality condition removed since there can be no degenerate triangles
        if sticks[i]+sticks[i+1] > sticks[i+2]: 
            return "possible"
    return "impossible"
        
N,sticks = int(input()),sorted(map(int,input().split())) #O(N log N) to sort
print(possibletriangle(N,sticks))

