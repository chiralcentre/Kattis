from sys import stdin,stdout

#find digit with lowest number of occurrences
#answer will be digit repeated * (occurrences + 1)
#in the case of zero, the answer has to be positive, so prepend a "1"

digits = stdin.readline().strip()
DAT = [0 for _ in range(10)] #DAT[i] stores the frequency of i
#set frequency of 0 to 1 so that 0 will not be output
DAT[0] = 1
for d in digits:
    DAT[int(d)] += 1
#frequency cannot exceed 1000
lowest,index = 100000,-1
for i in range(10):
    if DAT[i] < lowest:
        lowest = DAT[i]
        index = i
if index == 0:
    stdout.write("1")
    lowest -= 1 #subtract the one added at the start
for i in range(lowest+1):
    stdout.write(str(index))
