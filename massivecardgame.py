from sys import stdin,stdout
# search for leftmost index of smallest element >= x
def binary_search_greater_or_equal(arr,arrlen,x):
    low,high = 0,arrlen-1
    ans = arrlen
    while low <= high:
        mid = (low + high)//2
        if arr[mid] < x:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    return ans

# search for leftmost index of smallest element > x
def binary_search_strictly_greater(arr,arrlen,x):
    low,high = 0,arrlen - 1
    ans = arrlen #ans is initialised to arrlen in case x >= max(arr)
    while low <= high:
        mid = (low+high)//2
        if arr[mid] <= x:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    return ans

N = int(stdin.readline())

cards = sorted(list(map(int,stdin.readline().split())))
lowest,highest = cards[0],cards[-1]
for _ in range(int(stdin.readline())):
    L,R = map(int,stdin.readline().split())
    if L > highest or R < lowest:
        stdout.write('0\n')
    else:
        if L < lowest:
            L = lowest
        if R > highest:
            R = highest
        stdout.write(str(binary_search_strictly_greater(cards,N,R)-binary_search_greater_or_equal(cards,N,L))+'\n')
          
       
        
    
    
                
