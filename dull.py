from sys import stdin,stdout

while True:
    line = stdin.readline().strip()
    if line == "0":
        break
    N,P,S = map(int,line.split())
    sizes = list(map(int,stdin.readline().split()))
    programs = []
    for _ in range(P):
        s,reqs = stdin.readline().split()
        L = []
        for r in reqs:
            L.append(ord(r) - ord('A'))
        programs.append([int(s),L])
    transitions = list(map(int,stdin.readline().split()))
    ans,curr,active,loaded,depend = 0,0,{},set(),{}
    for q in transitions:
        if q > 0:
            q -= 1
            for idx in programs[q][1]:
                if idx not in loaded:
                    loaded.add(idx)
                    curr += sizes[idx]
                depend[idx] = depend.get(idx,0) + 1
            curr += programs[q][0]
            ans = max(curr,ans)
            active[q] = active.get(q,0) + 1
        elif q < 0:
            q = abs(q) - 1
            curr -= programs[q][0]
            active[q] -= 1
            if active[q] == 0:
                active.pop(q)
            for idx in programs[q][1]:
                depend[idx] -= 1
                if depend[idx] == 0:
                    depend.pop(idx)
                    loaded.discard(idx)
                    curr -= sizes[idx]
    stdout.write(f"{ans}\n")
            
