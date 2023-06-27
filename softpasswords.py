def solve(S,P):
    if S == P:
        return "Yes"
    if len(S) == len(P):
        #check for equality after reversing case
        for i in range(len(P)):
            r = P[i]
            if P[i].isalpha():
                r = P[i].lower() if P[i].isupper() else P[i].upper()
            if r != S[i]:
                return "No"
        return "Yes"
    elif len(S) == len(P) + 1:
        if S[0].isdigit() and S[1:] == P:
            return "Yes"
        if S[-1].isdigit() and S[:-1] == P:
            return "Yes"
        return "No"
    return "No"

S,P = input().strip(),input().strip()
print(solve(S,P))
