for i in range(int(input())):
    n1,poly1 = int(input()),list(map(int,input().split()))
    n2,poly2 = int(input()),list(map(int,input().split()))
    product = [0 for _ in range(n1+n2+1)] #maximum power is n1+n2
    for j in range(n1+1): #length of poly1
        for k in range(n2+1): #length of poly2
            counter = poly1[j]*poly2[k]
            product[j+k] += counter
    print(n1+n2)
    print(' '.join(map(str,product)))
