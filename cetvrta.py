def missing_number(lst):
    # in each list of x and y coordinates, there should be two numbers that appear twice
    dict1 = {num: 0 for num in lst}
    for num in lst:
        dict1[num] += 1
    for key,value in dict1.items():
        if value == 1:
            return key
        
x,y = [],[]
for _ in range(3):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

print(f'{missing_number(x)} {missing_number(y)}')
