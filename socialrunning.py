from sys import stdin,stdout

#first and last runner will run alone
N = int(stdin.readline())
distances = [int(stdin.readline()) for _ in range(N)]
lowest = 10**9
for i in range(N):
    first,last = distances[i],distances[(i + N - 2) % N]
    lowest = min(lowest,first + last)
stdout.write(f"{lowest}\n")
    
