from sys import stdin,stdout

#sort the array
#largest possible absolute difference is max(arr) - min(arr)
#put max(arr) in nth place and min(arr) in n - 1th place. No other difference will 
#repeat for remaining elements
N = int(stdin.readline())
lst = sorted(map(int,stdin.readline().split()))
new_arr = [-1 for _ in range(N)]
for i in range(N//2):
    new_arr[N - 1 - i*2] = lst[N - 1 - i]
    new_arr[N - 2 - i*2] = lst[i]
if N%2:
    new_arr[0] = lst[N//2]
stdout.write(' '.join(str(r) for r in new_arr))

