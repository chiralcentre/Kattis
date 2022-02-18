for _ in range(int(input())):
    command = input().split()
    print(' '.join(command[2:])) if len(command) > 2 and command[0] == 'simon' and command[1] == 'says' else print()
   
