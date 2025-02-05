from sys import stdin,stdout

def getSurname(name):
    for i in range(len(name)):
        if name[i].isupper():
            return name[i:]
    raise Exception("not supposed to happen")

names = [stdin.readline().strip() for _ in range(int(stdin.readline()))]
for i in range(len(names)):
    names[i] = (names[i],getSurname(names[i]))
names.sort(key = lambda x: x[1])
stdout.write("\n".join(p[0] for p in names))
