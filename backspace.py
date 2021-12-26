string = list(input().strip())
lst = []
for char in string:
    if char != '<':
        lst.append(char)
    else:
        lst.pop()
print(''.join(lst))
