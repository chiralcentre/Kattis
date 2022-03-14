from sys import stdin,stdout

a = int(stdin.readline())
stdout.write(f'{100/a}\n')
stdout.write(f'{100/(100-a)}\n')
