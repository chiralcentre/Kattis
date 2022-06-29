from sys import stdin,stdout

case = 0
while True:
    n = int(stdin.readline())
    case += 1
    if n == 0:
        break
    animals = {}
    for i in range(n):
        description = stdin.readline().split()
        kind = description[-1].lower()
        animals[kind] = 1 if kind not in animals else animals[kind] + 1
    lst = sorted(list(animals.items()),key = lambda x: x[0]) #sort by alphabetical order
    stdout.write(f"List {case}:\n")
    for animal,count in lst:
        stdout.write(f"{animal} | {count}\n")
