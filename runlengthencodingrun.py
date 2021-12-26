def RLE(s):
    string = ''
    while s:
        char,counter = s[0], 1
        s = s[1:]
        while len(s) > 0 and s[0] == char :
            counter += 1
            s = s[1:]
        string += char + str(counter)
    return string

def RLD(s):
    return s if s == '' else s[0]*int(s[1]) + RLD(s[2:])

def runlength(s):
    lst = s.split()
    if lst[0] == 'E': # encoding
        return RLE(lst[1])
    elif lst[0] == 'D': #decoding
        return RLD(lst[1])

print(runlength(input()))
