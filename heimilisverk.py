from sys import stdin,stdout

seen = set()
for _ in range(int(stdin.readline())):
    chore = stdin.readline().strip()
    if chore not in seen:
        stdout.write(f"{chore}\n")
        seen.add(chore)