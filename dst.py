for i in range(int(input())):
    testcase = input().split()
    direction = testcase[0]
    D,H,M = list(map(int,testcase[1:]))
    if direction == 'F':
        if M + D < 60:
            M += D
        else:
            H = (H+((M+D)//60))%24
            M = (M+D)%60
    else: #go backwards
        if M - D >= 0:
            M -= D
        else:
            while M - D < 0:
                M += 60
            H = (H - (M//60))%24
            M -= D       
    print(f'{H} {M}')
