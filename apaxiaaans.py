def apaxia(s1):
    s2 = ''
    while s1:
        char = s1[0]
        s2 += s1[0]
        s1 = s1[1:]
        while len(s1) >= 1 and s1[0] == char:
            s1 = s1[1:]
    return s2

name = input()
print(apaxia(name))
