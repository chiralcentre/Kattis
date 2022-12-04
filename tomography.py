from sys import stdin,stdout

def possible(row_sums,col_sums):
    #O(mn log n + mn)
    for k in row_sums:
        col_sums = sorted(col_sums,reverse=True)
        if k > len(col_sums):
            return "No"
        if k == 0:
            continue
        #k > 0, but we do not have k columns with non zero sums
        if col_sums[k - 1] == 0:
            return "No"
        #subtract 1 from k largest column sums
        for i in range(k):
            col_sums[i] -= 1
    for c in col_sums:
        if c != 0:
            return "No"
    return "Yes"
        
#Havel-Hakimi theorem       
#choose any row with number k, remove from list of totals
#subtract 1 from the k largest column sums
#repeat, and if at any point there isn't k columns with non-zero sums, no such matrix can exist
#values of m and n not required
stdin.readline().split() 
row_sums = list(map(int,stdin.readline().split()))
col_sums = list(map(int,stdin.readline().split()))
stdout.write(possible(row_sums,col_sums))


