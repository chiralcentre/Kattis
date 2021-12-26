from math import floor

m = int(input())
mbase = floor(round(m**(1/3),3))
busnums = set() # a set is used to reduce search time
largest = -1

for i in range(1,mbase+1):
    for j in range(i,mbase+1):
        num = i**3 + j**3
        if num <= m:
            if num in busnums:
                if num > largest:
                    largest = num
            else:
                busnums.add(num)
        else:
            break #break the loop when the sum of cubes is larger than m
        
print(largest) if largest > -1 else print('none')

