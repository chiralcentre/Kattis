from sys import stdin,stdout

n = int(stdin.readline())
single,pairing = set(),{}
for i in range(n):
    names = stdin.readline().split()
    if len(names) == 1:
        single.add(names[0])
    elif len(names) == 2:
        pairing[names[0]] = names[1]
for _ in range(int(stdin.readline())):
    name = stdin.readline().strip()
    if name in single:
        stdout.write("Jebb\n")
    elif name in pairing:
        stdout.write(f"Neibb en {name} {pairing[name]} er heima\n")
    else:
        stdout.write("Neibb\n")
