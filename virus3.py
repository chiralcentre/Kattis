def checkIsSubsequence(s1,s2):
    n, m = len(s1), len(s2)
    i, j = 0, 0
    while i < n and j < m:
        if s1[i] == s2[j]:
            i += 1
        j += 1
    return i == n
    
F,H = input().strip(),input().strip()
print("Ja") if checkIsSubsequence(F,H) else print("Nej")