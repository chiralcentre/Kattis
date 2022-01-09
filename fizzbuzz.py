X,Y,N = map(int,input().split())

for i in range(1,N+1):
    if i%X and i%Y:
        print(i)
    elif not i%X and i%Y:
        print('Fizz')
    elif i%X and not i%Y:
        print('Buzz')
    else: # divisible by both X and Y
        print('FizzBuzz')
