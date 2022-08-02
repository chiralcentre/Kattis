from sys import stdin,stdout
# it is only possible if the max heights in the eastern and northern skylines are the same
stdin.readline()
stdout.write("possible\n") if max(map(int,stdin.readline().split())) == max(map(int,stdin.readline().split())) else stdout.write("impossible\n")
