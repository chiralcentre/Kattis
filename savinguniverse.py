from sys import stdin,stdout

for i in range(int(stdin.readline())):
    S = int(stdin.readline())
    engines = {stdin.readline().strip() for _ in range(S)}
    switch,seen = 0,set()
    for j in range(int(stdin.readline())):
        q = stdin.readline().strip()
        seen.add(q)
        if len(seen) == S:
            switch += 1
            seen = {q}
    stdout.write(f"Case #{i + 1}: {switch}\n")        
