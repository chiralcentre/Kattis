from sys import stdin,stdout

prefixes = {}
for _ in range(int(stdin.readline())): #O(A)
    string = stdin.readline().strip()
    for i in range(1,len(string)+1): #Maximum 10 iterations since each name is between 1 and 10 characters long
        prefixes[string[0:i]] = prefixes[string[0:i]] + 1 if string[0:i] in prefixes else 1

for _ in range(int(stdin.readline())): #O(B)
    p = stdin.readline().strip()
    stdout.write(f'{prefixes[p]}\n') if p in prefixes else stdout.write(f'0\n')
