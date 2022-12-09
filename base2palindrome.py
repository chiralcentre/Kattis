from collections import deque
# runs in O(n), assuming string concatenation runs in O(1) since the strings are relatively small
def getNthNumber(n):
    # stores the binary palindrome string
    q = deque([])
    if n == 1:
        return 1
    n -= 1 
    q.append("11")
    # runs till the nth binary palindrome number
    while q:       
        curr = q.popleft()
        n -= 1
        if n == 0:
            return int(curr,2)
        L = len(curr)    
        # if length is even, 0 and 1 can be added into the middle
        if len(curr) % 2 == 0:
            q.append(curr[0:L//2]+"0"+curr[L//2:])
            q.append(curr[0:L//2]+"1"+curr[L//2:])
        # if length is odd, add middle character into middle position again
        else:
            midChar = curr[L//2]
            q.append(curr[0:L//2]+midChar+curr[L//2:])
    return 0

print(getNthNumber(int(input())))

