n = int(input())
maximum,minimum = set(),set()
array = list(map(int,input().split()))
largest,lowest = -2147483648,2147483648 #index of largest number and smallest 32bit signed integer
# possible pivots are larger than all elements on the left and smaller than all elements on right
for i in range(n): #O(n)
    if array[i] > largest:
        largest = array[i]
        maximum.add(i)
for j in range(n-1,-1,-1): #O(n)
    if array[j] < lowest:
        lowest = array[j]
        minimum.add(j)
# intersection between the two sets contains the pivot
print(len(maximum.intersection(minimum))) #O(max(k,m)) where k and m are the lengths of maximum and minimum respectively
