#In general, if the two dice have n and m sides respectively, then the most likely total is 0.5*(m + n + 2).
#Credit to stackoverflow: Let a and b be the number of sides and assume a is less than (or equal to) b. Then all sums between a+1 and b+1 and have the same likelihood (of a/(a+b)) and that likelihood is also maximal. 
N,M = map(int,input().split())
for i in range(min(N,M)+1,max(N,M)+2):
    print(i)
