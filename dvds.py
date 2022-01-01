for i in range(int(input())):
    n,order = int(input()),list(map(int,input().split()))
    correct = 0
    for num in order: #check if DVDs are in the correct place
        if num == correct + 1:
            correct += 1
    print(n-correct)
    
