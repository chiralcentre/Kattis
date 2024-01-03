from sys import stdin,stdout

N = int(stdin.readline())
coins = list(map(int,stdin.readline().split()))
stdin.readline() # timings not needed
luigi_worlds = list(map(int,stdin.readline().split()))
# coins left assuming Luigi takes all coins from first world
remainder = sum(coins) - coins[luigi_worlds[0] - 1]
# guaranteed to win if sum of remaining coins apart from the first world Luigi visits > the coins from the world Luigi visits
# Mario can win by visiting the same worlds that Luigi visits after the first world in the same order
if remainder > coins[luigi_worlds[0] - 1]:
    stdout.write("1\n")
    stdout.write(" ".join(str(luigi_worlds[i]) for i in range(1,N)))
    stdout.write(f" {luigi_worlds[0]}\n")
else:
    stdout.write("0.25\n") if N == 2 else stdout.write("0.5\n")
    stdout.write(str(luigi_worlds[0]))
    for i in range(2,N):
        stdout.write(f" {luigi_worlds[i]}")
    if N > 1:
        stdout.write(f" {luigi_worlds[1]}")
    stdout.write("\n")

