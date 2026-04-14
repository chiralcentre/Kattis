# number of fully infected nodes follows Fibonacci sequence
# length of sequence is 46
infected,H = [0,1],pow(10,9)
while infected[-1] < H:
    infected.append(infected[-2] + infected[-1])
n = int(input())
ans = -1
for i in range(len(infected)):
    if infected[i] >= n:
        ans = i
        break
print(ans)
