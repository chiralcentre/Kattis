from sys import stdin,stdout

stdout.write("Gnomes:\n")
for _ in range(int(stdin.readline())):
    gnomes = list(map(int,stdin.readline().split()))
    gnomes_asc = sorted(gnomes)
    gnomes_desc = sorted(gnomes, reverse = True)
    if gnomes == gnomes_asc or gnomes == gnomes_desc:
        stdout.write("Ordered\n")
    else:
        stdout.write("Unordered\n")
