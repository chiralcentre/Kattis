for _ in range(int(input())):
    line = input().strip()
    print('skipped') if line == 'P=NP' else print((lambda x: int(x[0])+int(x[1]))(line.split('+')))
        
