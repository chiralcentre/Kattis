from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    words = stdin.readline().split()
    freq,best,letter = {},-1,None
    for w in words:
        f = freq.get(w[0],0) + 1
        freq[w[0]] = f
        if f > best or (f == best and w[0] < letter):
            best,letter = f,w[0]    
    stdout.write(f"{letter}\n")
