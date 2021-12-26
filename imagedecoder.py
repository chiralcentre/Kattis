def imagedecoder(lst):
    symbols = ['#','.']
    fsym = lst[0]
    symbols.remove(fsym)
    osym = symbols[0]
    lst = list(map(int,lst[1:]))
    for i in range(len(lst)):
        print(fsym*lst[i],end='') if not i%2 else print(osym*lst[i],end='') 
    print('')

#up to 10 images
for i in range(10):
    lines_num = int(input())
    if lines_num == 0:
        break
    if i != 0:
        print('') #new line to separate images
    counter,counts = 0,set()
    while counter < lines_num:
        inpt = input().strip().split()
        counts.add(sum(list(map(int,inpt[1:]))))
        imagedecoder(inpt)
        counter += 1
    if len(counts) > 1:
        print('Error decoding image')
    

        
        
    
    
