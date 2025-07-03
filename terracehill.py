from sys import stdin

N = int(stdin.readline())
terraces = list(map(int,stdin.readline().split()))
stack,ans = [(terraces[0],0)],0
for i in range(1,N):
    while stack and stack[-1][0] < terraces[i]:
        stack.pop()
    if stack and stack[-1][0] == terraces[i]:
        ans += i - stack[-1][1] - 1
    stack.append((terraces[i],i))
print(ans)
            
