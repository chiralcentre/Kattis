K = int(input())
prev,current = 0,1
for i in range(K-1):
    a = prev + current
    prev = current
    current = a
print(f'{prev} {current}') #fibonacci sequence
