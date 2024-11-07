from sys import stdin,stdout

def reverse(a, x, y):
    while x < y:
        a[x],a[y] = a[y],a[x]
        x += 1
        y -= 1
 
def sortArr(a, n):
    # collapse all consecutive duplicates into one
    arr,i = [],0
    while i < n:
        arr.append(a[i])
        j = i
        while j < n - 1 and a[j] == a[j + 1]:
            j += 1
        i = j + 1
    x, y = -1, -1
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if x == -1:
                x = i
            y = i + 1
    if x != -1:
        reverse(arr, x, y)
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                return False
    return True

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
stdout.write("Yes\n") if sortArr(arr,n) else stdout.write("No\n")

