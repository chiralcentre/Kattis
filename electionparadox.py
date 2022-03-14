from sys import stdin,stdout

N = int(stdin.readline())
cities = sorted(list(map(int,stdin.readline().split())))
won,votes = N//2,0
for i in range(N-1,N-1-won,-1): #assume losing party won the cities with the largest populations
    votes += cities[i] 
for j in range(N-1-won,-1,-1):
    votes += cities[j]//2
stdout.write(f'{votes}\n')
