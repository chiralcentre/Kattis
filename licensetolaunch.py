n = int(input())
spacejunk = list(map(int,input().split()))
lowest,index_min = spacejunk[0],0
for i in range(1,n):
    if spacejunk[i] < lowest:
        lowest = spacejunk[i]
        index_min = i
print(index_min)
