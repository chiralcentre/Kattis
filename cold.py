num = int(input())
temps = list(map(int,input().split()))
counter = 0
for temp in temps:
    if temp < 0:
        counter += 1
print(counter)
