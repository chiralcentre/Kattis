n = int(input())

birthdays = {}

for i in range(n):
    entry = input().split()
    day = entry[2]
    if day not in birthdays:
        birthdays[day] = [entry[0:2]]
    else:
        birthdays[day].append(entry[0:2])
        
counter,names = 0,[]
for value in birthdays.values():
    lst = sorted([[x,int(y)] for x,y in value],key = lambda x: x[1])
    names.append(lst[len(lst)-1][0])
    counter += 1

print(counter)
for name in sorted(names):
    print(name)
    
        
