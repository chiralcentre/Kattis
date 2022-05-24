from sys import stdin,stdout

def search(prev,adjList):
    if prev[-1] not in adjList:
        return "?"
    else:
        for name in adjList[prev[-1]]:
            if name[-1] not in adjList or (len(adjList[name[-1]]) == 1 and name[0] == name[-1]):
                return f"{name}!" #eliminate next player
        return adjList[prev[-1]][0] #return first name on list if there is any animal name that can be played

prev = stdin.readline().strip()
#an edge exists between a and b if a is the first letter of b
adjList = {}; n = int(stdin.readline())
for i in range(n):
    animal = stdin.readline().strip()
    if animal[0] in adjList:
        adjList[animal[0]].append(animal)
    else:
        adjList[animal[0]] = [animal]
stdout.write(search(prev,adjList))
