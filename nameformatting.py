from sys import stdin,stdout

first,last = stdin.readline().strip().split(", ")
stdout.write(last[0].upper())
stdout.write(". ")
stdout.write(first[0].upper() + first[1:])
