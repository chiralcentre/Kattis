from sys import stdin,stdout

while True:
    n,*p = map(int,stdin.readline().split())
    if n == 0:
        break
    for i in range(n):
        p[i] -= 1
    message = list(stdin.readline().strip("\n"))
    if len(message) % n:
        for i in range(n - len(message) % n):
            message.append(" ")
    ans = []
    for i in range(0,len(message),n):
        for j in range(0,n):
            ans.append(message[i + p[j]])
    stdout.write("\'")
    stdout.write("".join(ans))
    stdout.write("\'\n")
