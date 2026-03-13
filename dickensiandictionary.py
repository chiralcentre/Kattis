s = input().strip()
L,R = set("qwertasdfgzxcvb"),set("yuiophjklnm")
for i in range(1,len(s)):
    if not ((s[i] in L and s[i - 1] in R) or (s[i] in R and s[i - 1] in L)):
        print("no")
        break
else:
    print("yes")
