# code runs in O(n^2) time
n,m = map(int,input().split())
ducks =  [i for i in range(n)]
output,curr = [],0
while ducks:
    curr = (curr - 1 + m) % len(ducks)
    output.append(ducks.pop(curr))
    
order = [-1 for _ in range(n)]
for i in range(n):
    order[output[i]] = str(i + 1)
print(" ".join(order))
