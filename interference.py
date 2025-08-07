from sys import stdin,stdout

# code runs in O(n^2)
n,w = map(int,stdin.readline().split())
waves = []
for i in range(n):
    command = stdin.readline().split()
    if command[0] == "!":
        waves.append((int(command[1]),int(command[2]),int(command[3])))
    else:
        p = int(command[1])
        h = 0
        for s,l,a in waves:
            if s <= p <= s + l - 1:
                r = (p - s) % 4
                # height of wave is 0 when r = 1 or r = 3
                if r == 0:
                    h += a
                elif r == 2:
                    h -= a
        stdout.write(f"{h}\n")
