from sys import stdin,stdout

N,C = map(int,stdin.readline().split())
seq = list(map(int,stdin.readline().split()))
freq = {}
for num in seq:
    freq[num] = 1 if num not in freq else freq[num] + 1
#the inbuilt sorting function of Python is stable
sortedfreq = sorted(list(freq.items()),key = lambda x: x[1], reverse = True)
stdout.write(' '.join(' '.join([str(num)]*value) for num,value in sortedfreq))
