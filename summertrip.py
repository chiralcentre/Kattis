s,counter = input().strip(),0
for i in range(len(s)):
    unique_letters = {s[i]}
    for j in range(i+1,len(s)):
        if s[j] == s[i]: # stop searching since no further interval can be valid
            break
        else:
            if s[j] not in unique_letters:
                counter += 1
                unique_letters.add(s[j])
print(counter)
    
