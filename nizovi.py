from sys import stdin,stdout

def indent(num):
    for i in range(num):
        stdout.write(" ")

def print_arr(arr,spaces,comma):
    indent(spaces)
    stdout.write("{\n")
    spaces += 2
    for i in range(len(arr)):
        c = i < len(arr) - 1
        if isinstance(arr[i],list):
            print_arr(arr[i],spaces, c)
        else:
            indent(spaces)
            stdout.write(arr[i])
            if c: stdout.write(",")
            stdout.write("\n")
    spaces -= 2
    indent(spaces)
    stdout.write("},\n") if comma else stdout.write("}\n")

def parse(a,b,c):
    global S
    curr,p,i = c,a,a
    while i < b: #ignore starting and closing brackets
        if S[i] == ",":
            if p < i:
                curr.append(S[p:i])
            p = i + 1
        elif S[i] == "{": #find corresponding index of matching closing bracket
            j,unclosed = i,1 #unclosed represent the number of opening brackets unclosed
            while unclosed > 0:
                j += 1
                if S[j] == "{":
                    unclosed += 1
                if S[j] == "}":
                    unclosed -= 1
            curr.append([])
            parse(i + 1,j,curr[-1])
            i = j
            p = j + 1
        while p < len(S) and not S[p].isalpha():
            p += 1
        i += 1
    if p < i:
        curr.append(S[p:i])
    return curr

S = stdin.readline().strip()
parsed = parse(1,len(S) - 1,[])
print_arr(parsed,0,False)

