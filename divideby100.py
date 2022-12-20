from sys import stdin,stdout

N,M = list(stdin.readline().strip()),stdin.readline().strip()
index = len(N) - len(M)
if index < 0:
    stdout.write("0.")
    for i in range(abs(index)-1):
        stdout.write("0")
    for i in range(len(N)):
        stdout.write(N[i])
else:
    for i in range(index+1):
        stdout.write(N[i])
    back = []; end = 0
    for j in range(index+1,len(N)):
        back.append(N[j])
        if N[j] != "0":
            end = j - index - 1
    if end != 0:
        stdout.write(".")
        for i in range(end+1):
            stdout.write(back[i])
stdout.write("\n")
 
