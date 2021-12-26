def distracted(L,married,unmarried):
    if L == 0:
        return 0
    else: 
        unknown = {}
        for j in range(L):
            p1,p2 = input().split(' -> ')
            if p1 in married and p2 in unmarried:
                return 1
            elif p1 in married and p2 not in unmarried and p2 not in married:
                unknown[(p1,'m')] = (p2,'?')
            elif p1 not in unmarried and p1 not in married and p2 not in unmarried and p2 not in married:
                unknown[(p1,'?')] = (p2,'?')
            elif p1 not in unmarried and p1 not in married and p2 in unmarried:
                unknown[(p1,'?')] = (p2,'u')
        if len(unknown) > 0: #logic puzzle: if start of graph is married,end of graph is unmarried, and all middle nodes are unknown, it is guaranteed that a married person will have met an unmarried person.
            keys = set(unknown.keys())
            for key in keys:
                if key[1] == 'm':
                    temp = key
                    while unknown[temp] in keys:
                        temp = unknown[temp]
                        if unknown[temp][1] == 'u':
                            return 1
            return '?'  
        else: # no unknown relationships
            return 0
    

N,L = list(map(int,input().split()))

married,unmarried = set(),set()

for i in range(N):
    name,status = input().split()
    if status == 'm':
        married.add(name)
    elif status == 'u':
        unmarried.add(name)

print(distracted(L,married,unmarried))
