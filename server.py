n,T = map(int,input().split())
tasks = list(map(int,input().split()))
time,counter = 0,0
for i in range(n):
    if time + tasks[i] <= T:
        time += tasks[i]
        counter += 1
    else:
        break
print(counter)
