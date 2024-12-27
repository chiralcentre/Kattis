from sys import stdin,stdout

def solve(f1,f2):
    for i in range(len(f1)):
        for j in range(len(f2)):
            if i != j and f1[i] == f2[j]:
                return "YES"
    return "NO"

for _ in range(int(stdin.readline())):
    f1,f2 = list(map(int,stdin.readline().split())),list(map(int,stdin.readline().split()))
    stdout.write(f"{solve(f1,f2)}\n")
                
