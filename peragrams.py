#only one letter can have odd number of occurrences in a palindrome
string = input().strip()
letters = {}
for char in string:
    letters[char] = 1 if char not in letters else letters[char] + 1
#number of letters to remove = number of letters with odd occurrences - 1
print(max(sum(1 for key,value in letters.items() if value%2) - 1,0)) #cannot be negative
    

