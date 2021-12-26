lst = []
for i in range(5):
    inpt = list(map(int,input().split()))
    lst.append(sum(inpt))

print(f'{lst.index(max(lst))+1} {max(lst)}')
