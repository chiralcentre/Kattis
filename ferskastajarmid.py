from sys import stdin,stdout

n = int(stdin.readline())
meme,best = -1,-1
for i in range(n):
    file,a,b = stdin.readline().split()
    c = int(a) * int(b)
    if c > best:
        meme,best = file,c
    elif c == best and file < meme:
        meme = file
stdout.write(f"{meme}\n")

        
