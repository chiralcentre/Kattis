N = int(input())
expenses = 0
for num in list(map(int,input().split())):
    if num < 0:
        expenses += abs(num)
print(expenses)
