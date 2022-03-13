from sys import stdin,stdout

s1,s2,num = stdin.readline().strip(),stdin.readline().strip(),1
for i in range(len(s1)):
    if s1[i] != s2[i]:
        num *= 2
stdout.write(f'{num}\n')
