Y,P = input().strip().split()
vowels = {'a','i','o','u'}
if Y[-1] == 'e':
    print(f'{Y}x{P}')
elif Y[-1] in vowels:
    print(f'{Y[:-1]}ex{P}')
elif Y[-1] == 'x' and Y[-2] == 'e':
    print(f'{Y}{P}')
else:
    print(f'{Y}ex{P}')
    
