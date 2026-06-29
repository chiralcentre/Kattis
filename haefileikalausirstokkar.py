from sys import stdin,stdout

bad = {stdin.readline().strip() for _ in range(int(stdin.readline()))}
for _ in range(int(stdin.readline())):
    cards = [stdin.readline().strip() for i in range(6)]
    for c in cards:
        if c in bad:
            stdout.write("Hæfileikalaust Drasl\n")
            break
    else:
        stdout.write("Fínn Stokkur\n")
