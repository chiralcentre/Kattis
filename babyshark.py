line = input().strip().split()
best,curr,ans = 1,1,line[0]
for i in range(1,len(line)):
    if line[i] == line[i - 1]:
        curr += 1
        if curr > best:
            best,ans = curr,line[i]
    else:
        curr = 1
print(ans)
