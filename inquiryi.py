from sys import stdin,stdout

n = int(stdin.readline())
array = [int(stdin.readline()) for _ in range(n)]
prefix_square_sum,prefix_sum = [],[]
square_counter,counter = 0,0
#O(n)
for i in range(n):
    square_counter += array[i]**2
    counter += array[i]
    prefix_square_sum.append(square_counter)
    prefix_sum.append(counter)
#O(n)
maximal = 0
for i in range(n):
    maximal = max(prefix_square_sum[i]*(prefix_sum[n-1]-prefix_sum[i]),maximal)
stdout.write(f"{maximal}")
