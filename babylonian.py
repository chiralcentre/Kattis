n = int(input())

for i in range(n):
    num = input().split(',')
    counter = 0
    for j in range(len(num)):
        if num[j] != '':
            counter += int(num[j])*60**(len(num)-j-1)
    print(counter)
