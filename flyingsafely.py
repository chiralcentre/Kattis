from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n,m = map(int,stdin.readline().split())
    for i in range(m):
        stdin.readline() #exact information about pilot trajectory is not needed at all
    stdout.write(f'{n-1}\n') #n-1 pilots is the mininum number since graph is connected
