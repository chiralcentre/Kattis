C,P = map(int,input().split())
columns = list(map(int,input().split()))
ans = 0
for i in range(C):
    if P == 1:
        ans += 1 
        ans += (i >= 3 and columns[i] == columns[i-1] and columns[i] == columns[i-2] and columns[i] == columns[i-3])
    elif P == 2:
        ans += (i >= 1 and columns[i] == columns[i-1])
    elif P == 3:
        ans += (i >= 2 and columns[i] == columns[i-1] + 1 and columns[i] == columns[i-2] + 1)
        ans += (i >= 1 and columns[i] == columns[i-1] - 1)
    elif P == 4:
        ans += (i >= 2 and columns[i] == columns[i-1] and columns[i] == columns[i-2] - 1)
        ans += (i >= 1 and columns[i] == columns[i-1] + 1)
    elif P == 5:
        ans += (i >= 1 and columns[i] == columns[i-1] + 1)
        ans += (i >= 1 and columns[i] == columns[i-1] - 1)
        ans += (i >= 2 and columns[i] == columns[i-1] and columns[i] == columns[i-2])
        ans += (i >= 2 and columns[i] == columns[i-1] + 1 and columns[i] == columns[i-2])
    elif P == 6:
        ans += (i >= 2 and columns[i] == columns[i-1] and columns[i] == columns[i-2])
        ans += (i >= 2 and columns[i] == columns[i-1] and columns[i] == columns[i-2] + 1)
        ans += (i >= 1 and columns[i] == columns[i-1])
        ans += (i >= 1 and columns[i] == columns[i-1] - 2)
    else:
        ans += (i >= 2 and columns[i] == columns[i-1] and columns[i] == columns[i-2])
        ans += (i >= 2 and columns[i] == columns[i-1] - 1 and columns[i] == columns[i-2] - 1)
        ans += (i >= 1 and columns[i] == columns[i-1])
        ans += (i >= 1 and columns[i] == columns[i-1] + 2)
print(ans)
