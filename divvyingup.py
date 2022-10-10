from sys import stdin,stdout

stdin.readline() #n not needed
stdout.write("no") if sum(map(int,stdin.readline().split())) % 3 else stdout.write("yes")
