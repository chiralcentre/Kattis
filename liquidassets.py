from sys import stdin,stdout

n = int(stdin.readline())
words = stdin.readline().split()
vowels = {'a','e','i','o','u'}
for i in range(n):
    w = words[i]   
    temp,prev = [],w[0]
    temp.append(w[0])
    for j in range(1,len(w)):
        if w[j] not in vowels and w[j] != prev:
            temp.append(w[j])
        prev = w[j]
    if temp[-1] != w[len(w)-1]:
        temp.append(w[len(w)-1])
    words[i] = ''.join(temp)
stdout.write(' '.join(words))

    
