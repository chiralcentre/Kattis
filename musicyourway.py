from sys import stdin,stdout

attributes = stdin.readline().split()
songs = [stdin.readline().split() for _ in range(int(stdin.readline()))]
for i in range(int(stdin.readline())):
    if i > 0: stdout.write("\n")
    cmd = stdin.readline().strip()
    idx = attributes.index(cmd)
    stdout.write(' '.join(attr for attr in attributes) + "\n")
    songs = sorted(songs,key = lambda x: x[idx])
    stdout.write('\n'.join(' '.join(word for word in song) for song in songs) + "\n")
    
