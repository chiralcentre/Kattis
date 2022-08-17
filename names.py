#the maximum number of operations for a string is length/2
#reverse the string, and check for characters which differ from the supposed position in a palindrome
string = input().strip()
temp = string[::-1]
ans = len(string)//2
for i in range(len(string)):
    diff,k = 0,0
    for j in range(i,len(string)):
        if (string[j] != temp[k]):
            diff += 1
        k += 1
    diff //= 2
    ans = min(ans, diff + i)
print(ans)
