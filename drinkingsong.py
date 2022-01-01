N,beverage = int(input()),input().strip()
for i in range(N,0,-1):
    if i >= 2:
        print(f'{i} bottles of {beverage} on the wall, {i} bottles of {beverage}.')
        print(f'Take one down, pass it around, {i-1} bottles of {beverage} on the wall.') if i > 2 else print(f'Take one down, pass it around, {i-1} bottle of {beverage} on the wall.')
        print() #new line
    elif i == 1:
        print(f'{i} bottle of {beverage} on the wall, {i} bottle of {beverage}.')
        print(f'Take it down, pass it around, no more bottles of {beverage}.')
