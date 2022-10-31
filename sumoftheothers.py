from sys import stdin,stdout

for line in stdin:
    lst = list(map(int,line.split()))
    prefix_sum,running_sum = [],0
    for i in range(len(lst)):
        running_sum += lst[i]
        prefix_sum.append(running_sum)
    for j in range(len(lst)):
        if j == 0:
            if lst[j] == prefix_sum[len(lst)-1] - prefix_sum[j]:
                stdout.write(f"{lst[j]}\n")
                break
        elif 1 <= j <= len(lst) - 2:
            if lst[j] == prefix_sum[j-1] + prefix_sum[len(lst)-1] - prefix_sum[j]:
                stdout.write(f"{lst[j]}\n")
                break
        else:
             if lst[j] == prefix_sum[j-1]:
                stdout.write(f"{lst[j]}\n")
                break


