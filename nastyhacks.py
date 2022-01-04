for i in range(int(input())):
    r,e,c = map(int,input().split())
    print('advertise') if r+c < e else print('does not matter') if r+c == e else print('do not advertise')
