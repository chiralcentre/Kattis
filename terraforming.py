from sys import stdin

ocean,oxygen,temp = 0,0,-30
for i in range(int(stdin.readline())):
    p,c = stdin.readline().split()
    c = int(c)
    if p == "temperature":
        temp += c
    elif p == "ocean":
        ocean += c
    else:
        oxygen += c
print("liveable") if ocean >= 9 and oxygen >= 14 and temp >= 8 else print("not liveable")
