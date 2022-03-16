from sys import stdin,stdout

n,m = map(int,stdin.readline().split())
#Zi is proportional to 1/i, so f/Zi is proportional to f*i
songs = [(lambda f,s: (int(f)*i,i,s))(*stdin.readline().split()) for i in range(1,n+1)] #O(n)
#O(n log n) - sort by quality in ascending order, then sort by order of appearance in reverse so earliest song will be popped first
songs.sort(key = lambda x: (x[0],-x[1])) 
for j in range(m): #in order the songs are given
    stdout.write(f'{songs.pop()[2]}\n')
