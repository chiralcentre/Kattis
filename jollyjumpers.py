from sys import stdin,stdout

for line in stdin:
    n,*seq = map(int,line.split())
    diff = [False for _ in range(n-1)] #boolean array to keep track of which difference has not been chosen yet
    counter = 0
    for i in range(n-1):
        d = abs(seq[i]-seq[i+1]) - 1 #offset by 1 due to zero indexing
        if d <= n - 2 and not diff[d]:
            diff[d] = True
            counter += 1
    stdout.write("Jolly\n") if counter == n - 1 else stdout.write("Not jolly\n")
