# maximum 26 unique letters
weights = [1,3,3,5,5,5,7,7,7,7,7,9,9,9,9,9,9,9,9,11,11,11,11,11,11,11]
s = input().strip()
freq,unique = {},0
for char in s:
    char = char.upper()
    if char.isalpha():
        freq[char] = freq.get(char,0) + 1
        unique += 1
occurrences = sorted(freq.values(), key = lambda x: -x) # sort in descending order
print((unique - 1) * 3 + sum(weights[i] * occurrences[i] for i in range(len(occurrences))))
        
