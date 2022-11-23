from sys import stdin,stdout
from collections import Counter

#can only have a maximum of one letter of odd frequency
def canFormPalin(string):
    return len([char for char,freq in Counter(string).items() if freq % 2]) <= 1

def minSwaps(string):
    counter,start = 0,0
    s = list(string) #convert to mutable sequence for swapping
    while start < len(s)//2: #O(N^2), where N is length of string
        left = start
        right = len(s) - start - 1
        while left < right:
            if s[left] == s[right]:
                break
            else:
                right -= 1
        if left == right:
            #s[left] is character in middle of palindrome
            s[left],s[left+1] = s[left+1],s[left]
            counter += 1
        else:
            for j in range(right, len(string) - left - 1):
                s[j],s[j+1] = s[j+1],s[j]
                counter += 1
            start += 1
    return counter
        

for _ in range(int(stdin.readline())):
    string = stdin.readline().strip()
    stdout.write("Impossible\n") if not canFormPalin(string) else stdout.write(f"{minSwaps(string)}\n")
