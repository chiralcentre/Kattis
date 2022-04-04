from sys import stdin,stdout

current,missing = 1,False
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    while n != current:
        stdout.write(str(current)+'\n')
        current += 1
        missing = True
    current += 1    
if not missing:
    stdout.write("good job\n")
