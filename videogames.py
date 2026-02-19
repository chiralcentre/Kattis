from sys import stdin,stdout

games = {"alice": {"fishing"}, "bob": {"golf"}, "charlie": {"hockey"}}
for _ in range(int(stdin.readline())):
    a,b = stdin.readline().strip("\n").split(" wants to play ")
    if b not in games[a]:
        owner = None
        for k,v in games.items():
            if b in v:
                owner = k
                break
        games[a].add(b)
        games[owner].remove(b)
        stdout.write(f"{a} borrows {b} from {owner}\n")
    else:
        stdout.write(f"{a} already has {b}\n")
