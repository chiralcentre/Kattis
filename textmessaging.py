from sys import stdin,stdout

for i in range(int(stdin.readline())):
    P,K,L = map(int,stdin.readline().split())
    #sort the frequencies, assign highest frequencies to the first letter of key
    freq = sorted(map(int,stdin.readline().split()))
    total,curr,used = 0,1,0
    for j in range(L - 1, -1, -1):
        total += curr * freq[j]
        used += 1
        if used == K:
            curr += 1
            used = 0
    stdout.write(f'Case #{i + 1}: {total}\n')
