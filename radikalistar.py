from sys import stdin,stdout

n,q = map(int,stdin.readline().split())
# the initial group is group 1
# groups[k] = group of person k
# groupings[i] = all members in group i
group_num,groups,groupings = 1,[1 for _ in range(n)],{1: {i for i in range(n)}}
for i in range(q):
    op,*line = stdin.readline().split()
    if op == "r": # operation runs in O(t) time
        _,*rest = map(lambda x: int(x) - 1,line)
        new_groups = {}
        for num in rest:
            old_group = groups[num]
            if old_group not in new_groups:
                new_groups[old_group] = {num}
            else:
                new_groups[old_group].add(num)
            groupings[old_group].remove(num)
            if len(groupings[old_group]) == 0:
                groupings.pop(old_group)
        for key,value in new_groups.items():
            group_num += 1
            for num in value:
                groups[num] = group_num
            groupings[group_num] = value
    elif op == "m":
        group = groups[int(line[0]) - 1]
        stdout.write(" ".join(str(num + 1) for num in groupings[group]))
        stdout.write("\n")
    else: # 's'
        stdout.write(f"{len(groupings)}\n")
        
