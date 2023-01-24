from sys import stdin,stdout

def printColumnHeader():
    stdout.write("NAME                ")
    stdout.write("       BIB")
    stdout.write("    SPLIT1")
    stdout.write("      RANK")
    stdout.write("    SPLIT2")
    stdout.write("      RANK")
    stdout.write("    FINISH")
    stdout.write("      RANK\n")
    
while True:
    n = int(stdin.readline())
    if n == 0: break
    mappings = {"S1": 0, "S2": 1, "F": 2}
    bibs,timings,ranks = [],[{} for _ in range(3)],[{} for _ in range(3)]
    for _ in range(n):
        first,last,b = stdin.readline().split()
        bibs.append((last,first,b))
    #sort bibs by last name, followed by first name
    bibs.sort(key = lambda x: (x[0],x[1]))
    for i in range(3*n):
        b,location,time = stdin.readline().split()
        M,S = map(int,time.split(":"))
        convertedTime = 60*M + S
        timings[mappings[location]][b] = (b,time,convertedTime)
    for i in range(3):
        t = sorted(timings[i].items(),key = lambda x: x[1][2]) #sort by convertedTime
        r,j = 1,0
        while j < n:
            consec = 1
            while j + 1 < n and t[j][1][2] == t[j+1][1][2]:
                consec += 1
                j += 1
            for k in range(consec - 1,-1,-1):
                ranks[i][t[j - k][0]] = r
            r += consec
            j += 1
    #print column header
    printColumnHeader()
    for x,y,z in bibs:
        #print name
        s = x + ", " + y
        stdout.write(s)
        for i in range(25 - len(s)): stdout.write(" ")
        #print bib number
        stdout.write(z)
        for i in range(3):
            #print timing
            for j in range(5): stdout.write(" ")
            stdout.write(timings[i][z][1])
            #print rank
            r = str(ranks[i][z])
            for j in range(10 - len(r)): stdout.write(" ")
            stdout.write(r)
        stdout.write("\n")
    #print new line between testcases
    stdout.write("\n")
        
        
