from sys import stdin,stdout

def solve(string):
    pointer,num = 0,1
    while pointer < len(string):
        if int(string[pointer:pointer+len(str(num))]) != num:
            return str(num)
        pointer += len(str(num))
        num += 1
    return str(num)

stdin.readline()
string = stdin.readline().strip()
stdout.write(solve(string))
