from sys import stdin,stdout

coords = {"q": (0,0), "w": (0,1), "e": (0,2), "r": (0,3),
          "t": (0,4), "y": (0,5), "u": (0,6), "i": (0,7),
          "o": (0,8), "p": (0,9), "a": (1,0), "s": (1,1),
          "d": (1,2), "f": (1,3), "g": (1,4), "h": (1,5),
          "j": (1,6), "k": (1,7), "l": (1,8), "z": (2,0),
          "x": (2,1), "c": (2,2), "v": (2,3), "b": (2,4),
          "n": (2,5), "m": (2,6)}

def dist(first,second):
    a,b = coords[first]
    c,d = coords[second]
    return abs(a - c) + abs(b - d)

for _ in range(int(stdin.readline())):
    word, L = stdin.readline().split()
    L = int(L)
    word_dist = []
    for i in range(L):
        w = stdin.readline().strip()
        d = sum(dist(w[j],word[j]) for j in range(len(word)))
        word_dist.append((w,d))
    word_dist.sort(key = lambda x: (x[1],x[0]))
    for w,d in word_dist:
        stdout.write(f"{w} {d}\n")
            
