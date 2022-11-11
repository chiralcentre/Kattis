from sys import stdin,stdout

W,P = map(int,stdin.readline().split())
partitions = [0]
partitions.extend(list(map(int,stdin.readline().split())))
partitions.append(W)
possibilities = set()
for i in range(P + 1):
    for j in range(i+1,P+2):
        possibilities.add(partitions[j] - partitions[i])
stdout.write(" ".join(str(width) for width in sorted(possibilities)))
