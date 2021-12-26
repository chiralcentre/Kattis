N = int(input())
numbers = sorted(list(map(int,input().split())))
lst,grouped = [],[]
while numbers:
    num = numbers.pop(0)
    if not lst:
        lst.append(num)
    else:
        if num == lst[-1] + 1:
            lst.append(num)
        else:
            grouped.append(lst)
            lst = [num]
grouped += [lst]

result = []
for elem in grouped:
    if len(elem) > 2:
        result.append(f'{elem[0]}-{elem[-1]}')
    elif len(elem) == 2: 
        result += [str(elem[0]),str(elem[1])]
    elif len(elem) == 1:
        result.append(str(elem[0]))
print(' '.join(result))

