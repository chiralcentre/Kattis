from sys import stdin,stdout

p = int(stdin.readline())
species_planets,visitors = {},{}
for i in range(p):
    P,n,*sp = stdin.readline().split()
    for j in range(int(n)):
        species_planets[sp[j]] = P
    visitors[P] = 0
for i in range(int(stdin.readline())):
    m,r = stdin.readline().split()
    visitors[species_planets[r]] += int(m)
for planet,number in sorted(visitors.items()):
    stdout.write(f"{planet} {number}\n")
