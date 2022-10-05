from sys import stdin,stdout

n = int(stdin.readline())
tiles = sorted(map(int,stdin.readline().split()))
lowest = sum((tiles[i] - tiles[i+1])**2 for i in range(n-1))
stdout.write(f"{lowest}")
