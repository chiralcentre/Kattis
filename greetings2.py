s = list(input().strip())
e_count = s.count('e')
print(s[0] + e_count*2*'e' + s[-1])
