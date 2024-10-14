from sys import stdin,stdout

N,M = map(int,stdin.readline().split())
names = stdin.readline().split()
hunter = {names[0]}
cheated = set()
for i in range(M):
    line = stdin.readline().split()
    if line[0] not in hunter:
        cheated.add(line[0])
    else:
        hunter.remove(line[0])
    hunter.add(line[2])
stdout.write(f"{len(cheated)}\n")
stdout.write(" ".join(sorted(cheated)))
stdout.write("\n")
