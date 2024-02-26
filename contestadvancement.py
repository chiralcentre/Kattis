from sys import stdin,stdout

# final teams must be output in rank order
# tuples containing two values are compressed into a single value to save time in sorting
n,k,c = map(int,stdin.readline().split())
advanced,school_wins,rem = [],[0 for _ in range(n + 1)],[]
for i in range(n):
    t,s = map(int,stdin.readline().split())
    t -= 1
    if school_wins[s] < c and len(advanced) < k:
        advanced.append(i * n + t)
        school_wins[s] += 1
    else:
        rem.append((t,s,i))
if len(advanced) < k:
    for t,s,r in rem:
        advanced.append(r * n + t)
        if len(advanced) == k:
            break
stdout.write("\n".join(str(team_id % n + 1) for team_id in sorted(advanced)))
