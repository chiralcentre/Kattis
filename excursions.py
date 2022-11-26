from sys import stdin,stdout,setrecursionlimit

#increase recursion limit to prevent stack overflow
setrecursionlimit(10**5)

#minimum number of adjacent swaps = number of inversions
#code runs in O(n log n) where n is length of string
def mergeAndCountInv(start,mid,end,arr):
    size = end - start + 1
    #use auxillary array to store final sorted subarray
    sortedArr = [-1 for _ in range(size)]
    invCount,leftIdx,rightIdx,idx = 0,start,mid+1,0
    #merge two sorted arrays into one sorted array
    while leftIdx <= mid and rightIdx <= end:
        if arr[leftIdx] <= arr[rightIdx]:
            sortedArr[idx] = arr[leftIdx]
            leftIdx += 1
            invCount += rightIdx - mid - 1
        else:
            sortedArr[idx] = arr[rightIdx]
            rightIdx += 1
        idx += 1
    while leftIdx <= mid:
        sortedArr[idx] = arr[leftIdx]
        idx += 1; leftIdx += 1
        invCount += end - mid
    while rightIdx <= end:
        sortedArr[idx] = arr[rightIdx]
        idx += 1; rightIdx += 1
    for i in range(start,end+1):
        arr[i] = sortedArr[i-start]
    return invCount

def sortAndCountInv(start,end,arr):
    if start == end:
        return 0
    mid = start + (end - start) // 2
    return sortAndCountInv(start,mid,arr) + sortAndCountInv(mid+1,end,arr) + mergeAndCountInv(start,mid,end,arr)

line = list(map(int,list(stdin.readline().strip())))
stdout.write(str(sortAndCountInv(0,len(line)-1,line)))
