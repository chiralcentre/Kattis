from sys import stdin,stdout

mappings = {
    **{str(i): i for i in range(10)},        # Map '0' to '9' -> 0 to 9
    **{chr(i): i - 87 for i in range(97, 123)},  # Map 'a' to 'z' -> 10 to 35
    **{chr(i): i - 29 for i in range(65, 91)}    # Map 'A' to 'Z' -> 36 to 61
}

def getLexicoSmallerString(s1,s2):
    return 0 if s1 < s2 else 1

# guaranteed to return a result since strings are distinct
def getBase62SmallerString(s1,s2):
    if len(s1) != len(s2):
        return 0 if len(s1) < len(s2) else 1
    else:
        for i in range(len(s1)):
            u1,u2 = mappings[s1[i]],mappings[s2[i]]
            if u1 < u2:
                return 0
            elif u1 > u2:
                return 1
        
        
for _ in range(int(stdin.readline())):
    s1,s2 = stdin.readline().strip(),stdin.readline().strip()
    r1,r2 = getLexicoSmallerString(s1,s2),getBase62SmallerString(s1,s2)
    stdout.write("YES\n") if r1 == r2 else stdout.write("NO\n")
