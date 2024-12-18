moves = [1,2,3,4,5,
         6,7,8,9,10,
         11,12,13,14,15,
         16,17,18,19,20,
         25,50]
res_moves = [1,2,3,4,5,
             6,7,8,9,10,
             11,12,13,14,15,
             16,17,18,19,20,
             50]

visited = [None for _ in range(502)]
# one throw, 21 combinations
for m3 in res_moves:
    res = 2 * m3 if m3 != 50 else m3
    if not visited[res]:
        visited[res] = f"double {m3}" if m3 != 50 else "bullseye"

# two throws, 62 * 21 = 1302 combinations
for m2 in moves:
    for m3 in res_moves:
        b,c = [],[]
        if m2 != 25 and m2 != 50:
            b.append((m2,f"single {m2}"))
            b.append((2 * m2,f"double {m2}"))
            b.append((3 * m2,f"triple {m2}"))
        elif m2 == 25:
            b.append((m2,f"single bull"))
        elif m2 == 50:
            b.append((m2,"bullseye"))
        if m3 != 50:
            c.append((2 * m3,f"double {m3}"))
        elif m3 == 50:
            c.append((m3,"bullseye"))
        for x2,r2 in b:
            for x3,r3 in c:
                res = x2 + x3
                if visited[res] == None:
                    visited[res] = r2 + "\n" + r3

# three throws, at most 62 * 62 * 21 = 80724 combinations
for m1 in moves:
    for m2 in moves:
        for m3 in res_moves:
            a,b,c = [],[],[]
            if m1 != 25 and m1 != 50:
                a.append((m1,f"single {m1}"))
                a.append((2 * m1,f"double {m1}"))
                a.append((3 * m1,f"triple {m1}"))
            elif m1 == 25:
                a.append((m1,f"single bull"))
            elif m1 == 50:
                a.append((m1,"bullseye"))
            if m2 != 25 and m2 != 50:
                b.append((m2,f"single {m2}"))
                b.append((2 * m2,f"double {m2}"))
                b.append((3 * m2,f"triple {m2}"))
            elif m2 == 25:
                b.append((m2,f"single bull"))
            elif m2 == 50:
                b.append((m2,"bullseye"))
            if m3 != 50:
                c.append((2 * m3,f"double {m3}"))
            elif m3 == 50:
                c.append((m3,"bullseye"))
            for x1,r1 in a:
                for x2,r2 in b:
                    for x3,r3 in c:
                        res = x1 + x2 + x3
                        if visited[res] == None:
                            visited[res] = r1 + "\n" + r2 + "\n" + r3
T = int(input())
print("impossible") if visited[T] == None else print(visited[T])
                
            
            
