from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n,categories,counter = int(stdin.readline()),{},1
    for i in range(n):
        name,x = stdin.readline().split() #no need to keep track of name since all names are distinct
        #start from 2 since if there are n items in a category, there are n+1 options, including the option to take nothing
        categories[x] = 2 if x not in categories else categories[x] + 1
    for key in categories:
        counter *= categories[key]
    stdout.write(f'{counter-1}\n') #remove 1 to account for the possibility that no disguise was chosen
