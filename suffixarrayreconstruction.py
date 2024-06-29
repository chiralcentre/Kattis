from sys import stdin,stdout

def process_line(output,p,suffix):
    p,split_suffix = int(p),suffix.split("*")
    if len(split_suffix) == 1: # no * present
        for j in range(len(suffix)):
            if output[j + p - 1] and output[j + p - 1] != suffix[j]:
                return False
            else:
                output[j + p - 1] = suffix[j]
    else:
        s1,s2 = split_suffix[0],split_suffix[1]
        p1,p2 = p,len(output) - len(s2) + 1
        for j in range(len(s1)):
            if output[j + p1 - 1] and output[j + p1 - 1] != s1[j]:
                return False
            else:
                output[j + p1 - 1] = s1[j]
        for j in range(len(s2)):
            if output[j + p2 - 1] and output[j + p2 - 1] != s2[j]:
                return False
            else:
                output[j + p2 - 1] = s2[j]
    return True

def check_output(output):
    for char in output:
        if char == "":
            return False
    return True

# fill in characters into output string and check if conflicts occur
# let sum of characters given for suffixes = S
# time complexity = O(S)
for _ in range(int(stdin.readline())):
    l,s = map(int,stdin.readline().split())
    output = ["" for i in range(l)]
    possible = True
    for i in range(s):
        p,suffix = stdin.readline().split()
        if possible:
            result = process_line(output,p,suffix)
            possible = result
    if possible:
        possible = check_output(output)
    stdout.write("".join(output)) if possible else stdout.write("IMPOSSIBLE")
    stdout.write("\n")
