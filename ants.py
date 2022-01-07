def distance_from_centre(d,c):
    return abs(c-d)

for _ in range(int(input())):
    l,n = map(int,input().split())
    ants = []
    while len(ants) < n:
        for ant in map(int,input().split()):
            ants.append(ant)
    ants = sorted(ants)
    lst1 = [distance_from_centre(d,l/2) for d in ants]
    lowest = l - ants[lst1.index(min(lst1))] if ants[lst1.index(min(lst1))] > l/2 else ants[lst1.index(min(lst1))] # travel to closer end
    highest = ants[lst1.index(max(lst1))] if ants[lst1.index(max(lst1))] > l/2 else l - ants[lst1.index(max(lst1))] # travel to farther end
    print(f'{lowest} {highest}')
