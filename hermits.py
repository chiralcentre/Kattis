from sys import stdin,stdout

N = int(stdin.readline())
#define S[a] as the total number of people who live on street a and all streets that cross street a
streets = list(map(int,stdin.readline().split()))
S = [streets[i] for i in range(N)]
for i in range(int(stdin.readline())):
    a,b = map(int,stdin.readline().split())
    a -= 1; b -= 1 #offset by 1 due to zero indexing
    S[a] += streets[b]; S[b] += streets[a]
#set 1 billion as an arbitraily large number
quietest,index = 1000000000,0
for i in range(N):
    if S[i] < quietest:
        quietest = S[i]
        index = i
stdout.write(f'{index+1}') #add back 1 to get 1 based index
