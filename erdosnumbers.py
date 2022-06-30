from sys import stdin,stdout
from collections import deque

authors,adjSet = [],{}
for line in stdin:
    first,*rest = line.split()
    authors.append(first)
    if first not in adjSet:
        adjSet[first] = set()
    for coauthor in rest:
        adjSet[first].add(coauthor)
        if coauthor not in adjSet:
            adjSet[coauthor] = {first}
        else:
            adjSet[coauthor].add(first)
#perform BFS from Paul Erdos
erdosnumbers = {name: -1 for name in adjSet}
erdosnumbers["PAUL_ERDOS"] = 0
frontier = deque(["PAUL_ERDOS"])
while frontier:
    u = frontier.popleft()
    for v in adjSet[u]:
        if erdosnumbers[v] == -1: #unvisited
            erdosnumbers[v] = erdosnumbers[u] + 1
            frontier.append(v)
for name in authors:
    stdout.write(f"{name} no-connection\n") if erdosnumbers[name] == -1 else stdout.write(f"{name} {erdosnumbers[name]}\n")
