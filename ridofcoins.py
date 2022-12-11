from sys import stdin,stdout

P = int(stdin.readline())
N1,N5,N10,N25 = map(int,stdin.readline().split())
best = -1
#one 25 cent coin can be replaced with 25 1 cent coins
#one 25 cent coin can be replaced with 5 5 cent coins
#two 25 cent coins can be replaced with 5 10 cent coints
#hence, start with at least N1 - 24 1 cent coins, N5 - 4 5 cent coins, and N10 - 4 10 cent coins and check if the rest can be paid with 25 cent coins.
for i in range(25):
    n1 = min(N1,P) - i
    if n1 < 0: break
    A = P - n1
    for j in range(5):
        n5 = min(N5,A//5) - j
        if n5 < 0: break
        B = A - 5*n5
        for k in range(5):
            n10 = min(N10,B//10) - k
            if n10 < 0: break
            C = B - 10*n10
            if not C%25 and C//25 <= N25 and n1 + n5 + n10 + C//25 > best:
                best = n1 + n5 + n10 + C//25
stdout.write("Impossible") if best == -1 else stdout.write(f"{best}")
            
    
