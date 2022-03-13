from sys import stdin,stdout
# use of memoisation ro reduce duplicate calculations
memo = {} 
for line in stdin:
    n,counter = int(line.split('/')[1]),0
    if n in memo:
        counter = memo[n]
    else:
        for x in range(n+1,2*n+1): #since n < x,y <= 2n
            if n*x%(x - n) == 0:
                counter += 1
        memo[n] = counter
    stdout.write(f'{counter}\n')
