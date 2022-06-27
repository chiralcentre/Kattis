from sys import stdin,stdout

#we can swap any pair of letters from the first and last k positions
string,k = stdin.readline().split()
letters = list(string)
k = int(k); n = len(letters)
if n >= 2*k: #all letters can be swapped
    stdout.write("Yes")
else:
    #there is no way to change any of the middle 2k - n letters, where n is length of string
    sorted_letters = sorted(letters) #O(n log n)
    possible = True
    for i in range(n-k,k,1):
        if sorted_letters[i] != letters[i]:
            possible = False
            break
    stdout.write("Yes") if possible else stdout.write("No")
    
