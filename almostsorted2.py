from sys import stdin,stdout

def reverse(a, x, y):
    while x < y:
        a[x],a[y] = a[y],a[x]
        x += 1
        y -= 1
 
 
def sortArr(a, n):
    x, y = -1, -1
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            if x == -1:
                x = i
            y = i + 1
    if x != -1:
        reverse(a, x, y)
        for i in range(n-1):
            if a[i] > a[i+1]:
                return False
    return True

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
stdout.write("Yes\n") if sortArr(arr,n) else stdout.write("No\n")
