from sys import stdin,stdout

def findking(gnomes):
    for i in range(2,gnomes[0]): #king cannot be in first and last position
        if gnomes[i]-gnomes[i-1] != 1:
            return i
        
n = int(stdin.readline())
for _ in range(n):
    gnomes = list(map(int,stdin.readline().split()))
    stdout.write(f'{findking(gnomes)}\n')
    
