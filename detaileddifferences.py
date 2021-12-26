for i in range(int(input())):
    s1,s2 = input().strip(),input().strip()
    output = ['.' if s1[i] == s2[i] else '*' for i in range(len(s1))]
    print(s1)
    print(s2)
    print(''.join(output))
