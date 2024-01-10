from sys import stdin,stdout

n,*array = map(int,stdin.readline().split())
maximum,pivots = set(),[]
largest,lowest = -2147483648,2147483648 #index of largest number and smallest 32bit signed integer
# possible pivots are larger than all elements on the left and smaller than all elements on right
for i in range(n): #O(n)
    if array[i] > largest:
        largest = array[i]
        maximum.add(i)
for j in range(n - 1,-1,-1): #O(n)
    if array[j] < lowest:
        lowest = array[j]
        if j in maximum:
            pivots.append(j)
stdout.write(f"{len(pivots)}")
if pivots:
    stdout.write(" ")
stdout.write(" ".join(str(array[pivots[i]]) for i in range(len(pivots) - 1, max(len(pivots) - 101,-1), -1)))
