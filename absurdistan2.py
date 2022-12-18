from math import comb
#there are (n-1)**n different graphs with n vertices and n edges
#note graph is not necessarily simple

N = int(input())
ans = [1]
for i in range(2,N+1):
    disconnected = sum(ans[j-1]*comb(i-1,j-1)*pow(i-j-1,i-j) for j in range(2,i-1))
    ans.append(pow(i-1,i) - disconnected)
print(ans[N-1]/pow(N-1,N))
