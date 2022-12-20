from sys import stdin,stdout

N,M = list(stdin.readline().strip()),stdin.readline().strip()
index = len(N) - len(M)
if index < 0:
    stdout.write("0.")
    for i in range(abs(index)-1):
        stdout.write("0")
    end = 0
    for i in range(len(N)):
        if N[i] != "0":
            end = i
    for i in range(end + 1):
        stdout.write(N[i])
else:
    for i in range(index+1):
        stdout.write(N[i])
    end = 0
    for j in range(index+1,len(N)):
        if N[j] != "0":
            end = j
    if end != 0:
        stdout.write(".")
        for i in range(index+1,end + 1):
            stdout.write(N[i])
stdout.write("\n")
 
