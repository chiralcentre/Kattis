from sys import stdin,stdout
from heapq import heappush,heappop

class Item:
    def __init__(self,idx,key):
        self.idx = idx
        self.key = key

    def __lt__(self,other):
        return self.key < other.key

# code runs in O(q log q) time
PQ,mappings = [],{}
m,q = map(int,stdin.readline().split())
for _ in range(q):
    line = stdin.readline().strip().split()
    if line[0] == "A":
        idx,key = int(line[1]),int(line[2])
        if idx not in mappings:
            heappush(PQ,Item(idx,key))
            mappings[idx] = key
        else:
            stdout.write("error\n")
            break
    elif line[0] == "C":
        # lazy update
        idx,key = int(line[1]),int(line[2])
        if idx in mappings:
            heappush(PQ,Item(idx,key))
            mappings[idx] = key
        else:
            stdout.write("error\n")
            break
    elif line[0] == "E":
        # remove duplicate or out of date copies
        while PQ and (PQ[0].idx not in mappings or mappings[PQ[0].idx] != PQ[0].key):
            heappop(PQ)
        if PQ:
            stdout.write(f"{PQ[0].idx}\n")
        else:
            stdout.write("error\n")
            break
    elif line[0] == "G":
        idx = int(line[1])
        if idx in mappings:
            stdout.write(f"{mappings[idx]}\n")
        else:
            stdout.write("error\n")
            break
    elif line[0] == "P":
        # remove duplicate or out of date copies
        while PQ and (PQ[0].idx not in mappings or mappings[PQ[0].idx] != PQ[0].key):
            heappop(PQ)
        if PQ:
            item = heappop(PQ)
            mappings.pop(item.idx)
            stdout.write(f"{item.idx}\n")
        else:
            stdout.write("error\n")
            break
    elif line[0] == "R":
        # lazy deletion
        idx = int(line[1])
        if idx in mappings:
            mappings.pop(idx)
        else:
            stdout.write("error\n")
            break
    else:
        stdout.write(f"{len(mappings)}\n")
