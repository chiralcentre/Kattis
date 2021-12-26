def basicprogramming2(A,N,t):
    if t == 1:
        s = set(A)
        for num in s:
            if 7777 - num in s:
                return 'Yes'
        return 'No'
    elif t == 2:
        return 'Unique' if len(set(A)) == N else 'Contains duplicate'
    elif t == 3:
        dict1 = {}
        for num in A:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
        for key,value in dict1.items():
            if value > N/2:
                return key
        return -1
    elif t == 4:
        return sorted(A)[N//2] if N%2 else f'{sorted(A)[N//2 - 1]} {sorted(A)[N//2]}'
    elif t == 5:
        lst = []
        for num in A:
            if num in range(100,1000):
                lst.append(num)
        lst2 = list(map(str,sorted(lst)))
        return ' '.join(lst2)
        

integers = list(map(int,input().split()))
p1,p2 = integers[0],integers[1]
array = list(map(int,input().split()))
print(basicprogramming2(array,p1,p2))
