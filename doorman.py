def check_exceed(M,person,limit):
    M += 1 if person == 'M' else -1
    return True if abs(M) > limit else False

def doorman(string,L):
    M,people = 0,0
    while string:
        if not check_exceed(M,string[0],L):
            M += 1 if string[0] == 'M' else -1
            people += 1
            string.pop(0)
        else:
            if len(string) > 1 and not check_exceed(M,string[1],L):
                M += 1 if string[1] == 'M' else -1
                people += 1
                string.pop(1)
            else:
                return people
    return people
            

X = int(input())
string = list(input().strip())
print(doorman(string,X))

