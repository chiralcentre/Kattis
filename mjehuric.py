pieces = list(map(int,input().split()))
while pieces != [1,2,3,4,5]:
    for i in range(4):
        if pieces[i] > pieces[i+1]:
            pieces[i],pieces[i+1] = pieces[i+1],pieces[i]
            print(' '.join(list(map(str,pieces))))

