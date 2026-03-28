from sys import stdin,stdout

# every playlist has a maximum of 100 songs
# MOVE and PLAY can be taken to run in O(1) time
N,T = map(int,stdin.readline().split())
playlists = [list(stdin.readline().strip()) for _ in range(N)]
for _ in range(T):
    line = stdin.readline().split()
    if line[0] == "PLAY":
        idx = int(line[1]) - 1
        original = set(playlists[idx])
        s = set(line[2])
        for song in s:
            if song not in original:
                stdout.write("NO\n")
                break
        else:
            stdout.write("YES\n")
    else:
        x,i,y = map(lambda x: int(x) - 1, line[1:])
        playlists[y].append(playlists[x].pop(i))
