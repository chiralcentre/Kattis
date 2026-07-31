from sys import stdin,stdout
from heapq import heappush,heappop

mappings = {"Green": 0, "Blue": 1, "Red": 2,
            "Black": 3, "DoubleBlack": 4}

class Mountain:
    def __init__(self,name,alt,diff):
        self.name = name
        self.alt = int(alt)
        self.level = mappings[diff]

    def __lt__(self, other):
        if not isinstance(other,Mountain):
            return NotImplemented
        return (self.level, self.alt) < (other.level, other.alt)

    def __repr__(self):
        return f"Mountain(name={self.name},alt={self.alt},level={self.level}"

def solve():
    # code runs in O(m log m) time
    k,m,y = map(int,stdin.readline().split())
    mountains = sorted([Mountain(*stdin.readline().split()) for _ in range(m)],key = lambda x: x.alt)
    favourite = stdin.readline().strip()
    # active is a min heap containing the hardest mountains available for consideration
    thresholds,active = [],[]
    for i in range(y):
        x = int(stdin.readline())
        thresholds.append((x,i))
    thresholds.sort(key = lambda x: -x[0]) # sort in reverse order of threshold
    ans,curr,found = [],m - 1,False
    for i in range(y):
        x,idx = thresholds[i]
        while curr >= 0 and mountains[curr].alt >= x:
            heappush(active,mountains[curr])
            if mountains[curr].name == favourite:
                found = True
            curr -= 1
        # len(active) >= k, as guaranteed by input constraints
        while len(active) > k:
            M = heappop(active)
            if M.name == favourite:
                # can terminate early, favourite mountain has been removed and cannot be added back again
                for j in range(i,y):
                    ans.append(("NO",thresholds[j][1]))
                return sorted(ans,key = lambda x: x[1])
        ans.append(("YES" if found else "NO",idx))
    return sorted(ans,key = lambda x: x[1])

for res,_ in solve():
    stdout.write(f"{res}\n")
