from sys import stdin,stdout

N,Q = map(int,stdin.readline().split())
initials = {}
for _ in range(N):
    name = stdin.readline().strip()
    first,last = name.split()
    pair = first[0] + last[0]
    if pair not in initials:
        initials[pair] = [name]
    else:
        initials[pair].append(name)
for _ in range(Q):
    pair = stdin.readline().strip()
    if pair not in initials:
        stdout.write("nobody\n")
    elif len(initials[pair]) == 1:
        stdout.write(f"{initials[pair][0]}\n")
    else:
        stdout.write("ambiguous\n")
