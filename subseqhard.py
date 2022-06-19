from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    stdin.readline() #read in blank line
    N = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    #prefix_sum[0] = 0; prefix_sum[i] = sum(arr[j] for j in range(i-1))
    #Note that the question can be rephrased as given an a prefix sum array B and a target sum of 47,
    #find the number of pairs i < j s.t. B[j] = B[i] + 47
    prefix_sum = [0 for _ in range(N+1)]; current = 0
    for i in range(N): #O(N)
        current += arr[i]
        prefix_sum[i+1] = current
    sol,H = 0,{}
    for j in range(N+1): #O(N)
        if prefix_sum[j] - 47 in H: #the sum has appeared
            sol += H[prefix_sum[j]-47]
        H[prefix_sum[j]] = 1 if prefix_sum[j] not in H else H[prefix_sum[j]] + 1
    stdout.write(f"{sol}\n")
        
