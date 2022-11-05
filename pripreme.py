from sys import stdin,stdout

#value of N not required
stdin.readline()
highest,total = 0,0
for t in map(int,stdin.readline().split()):
    total += t
    highest = max(highest,t)
stdout.write(str(highest*2)) if 2*highest > total else stdout.write(str(total))
