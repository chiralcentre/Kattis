from sys import stdin

addresses,tups = [],[]
while True:
    line = stdin.readline().strip("\n")
    if line == "q":
        break
    address,num = line.split()
    addresses.append(line)
    tups.append((address,num))
print(addresses)
print(tups)
