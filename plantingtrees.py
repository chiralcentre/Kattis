from sys import stdin,stdout

N = int(stdin.readline())
trees = sorted(map(int,stdin.readline().split()))
#plant trees that take the longest first
counter = 0
for i in range(N-1,-1,-1):
    counter += max(trees[i] + N - i - counter,0)
stdout.write(f"{counter + 1}")
