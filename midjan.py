from sys import stdin

n,m = map(int,stdin.readline().split())
mon,tues = stdin.readline().split(),stdin.readline().split()
mon_set,tues_set = set(mon),set(tues)
print(" ".join(x for x in mon if x not in tues_set))
print(" ".join(y for y in tues if y not in mon_set))
