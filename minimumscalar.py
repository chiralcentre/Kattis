from sys import stdin,stdout

for i in range(int(stdin.readline())):
    n = int(stdin.readline())
    v1 = sorted(map(int,stdin.readline().split()))
    v2 = sorted(map(int,stdin.readline().split()),reverse = True)
    MSP = sum(v1[i]*v2[i] for i in range(n))
    stdout.write(f"Case #{i+1}: {MSP}\n")
