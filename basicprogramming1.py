def basicprogramming1(A,N,t):
    if t == 1:
        return 7
    elif t == 2:
        if A[0] > A[1]:
            return 'Bigger'
        elif A[0] == A[1]:
            return 'Equal'
        else:
            return 'Smaller'
    elif t == 3:
        sort_lst = sorted(A[0:3])
        return sort_lst[1]
    elif t == 4:
        return sum(A)
    elif t == 5:
        counter = 0
        for num in A:
            if num%2 == 0:
                counter += num
        return counter
    elif t == 6:
        #ASCII code of 'a' is 97
        return ''.join([chr(97+i % 26) for i in A])
        '''
        #runtime is way slower but has same functionality
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        new_lst = list(map(lambda x: x%26,A))
        string = ''
        for num in new_lst:
            string += alphabet[num]
        return string
        '''
    elif t == 7:
        i,dict1 = 0,{}
        while True:
            i = A[i]
            if i not in dict1.keys():
                dict1[i] = 1
            else:
                return "Cyclic"
            if i > N-1:
                return "Out"
            elif i == N-1:
                return "Done"
         d = list(data)
        ''' #same functionality
        visited = [False]*N
        i = 0
        while True:
            if i >= N:
                return 'Out'
            if visited[i]:
                return 'Cyclic'
            if i == N-1:
                return 'Done'
            visited[i] = True
            i = A[i]
        '''
integers = list(map(int,input().split()))
p1,p2 = integers[0],integers[1]
array = list(map(int,input().split()))
print(basicprogramming1(array,p1,p2))
