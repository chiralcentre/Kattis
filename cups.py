from sys import stdin,stdout

cups = []
for _ in range(int(stdin.readline())):
    a,b = stdin.readline().split()
    try:
        cups.append((b,int(a)/2))
    except ValueError:
        cups.append((a,int(b)))
cups.sort(key = lambda x: x[1])        
stdout.write('\n'.join(c[0] for c in cups))
    

