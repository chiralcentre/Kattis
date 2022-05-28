from sys import stdin,stdout

precedence = {"rock":"scissors","scissors":"paper","paper":"rock"}
first = True
while True:
    firstLine = stdin.readline().split()
    if firstLine[0] == "0":
        break
    if first:
        first = False
    else:
        stdout.write("\n") #print new line between test cases
    n,k = int(firstLine[0]),int(firstLine[1])
    games = k*n*(n-1)//2
    wins,losses = [0 for i in range(n)],[0 for i in range(n)]
    for _ in range(games):
        p1,m1,p2,m2 = stdin.readline().split()
        p1 = int(p1) - 1; p2 = int(p2) - 1 #offset by 1 due to zero indexing
        if m1 != m2: #not a draw
            if precedence[m1] == m2:
                wins[p1] += 1; losses[p2] += 1
            elif precedence[m2] == m1:
                wins[p2] += 1; losses[p1] += 1
    for i in range(n):
        stdout.write("-\n") if wins[i] + losses[i] == 0 else stdout.write("{:.3f}".format(wins[i]/(wins[i]+losses[i]))+"\n")
            
