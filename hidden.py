from collections import deque

def solve(password,string):
    pw_curr,str_curr = 0,0
    while pw_curr < len(password) and str_curr <= len(string):
        if str_curr == len(string): #end of string is reached
            return "FAIL"
        elif string[str_curr] == password[pw_curr]:
            pw_curr += 1
            if pw_curr == len(password):
                return "PASS"
        else:
            for i in range(pw_curr + 1, len(password)):
                if password[i] == string[str_curr]:
                    return "FAIL"
        str_curr += 1
        
password,string = input().split()
print(solve(password,string))
