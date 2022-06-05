from sys import stdin,stdout

n = int(stdin.readline()); socks = stdin.readline().split()
auxiliary,moves = [],0
for s in socks:
    if auxiliary and auxiliary[-1] == s:
        auxiliary.pop()
    else:
        auxiliary.append(s)
    moves += 1
stdout.write(str(moves)) if not auxiliary else stdout.write("impossible")
