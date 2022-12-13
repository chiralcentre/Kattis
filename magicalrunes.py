from sys import stdin,stdout

def reversedBinary(num,length):
    ans = []
    while num:
        ans.append(str(num&1))
        num >>= 1
    for i in range(length - len(ans)):
        ans.append("0")
    return ans

#let A represent 0, and B represent 1
#then the string read from right to left is a binary number
#changing leftmost rune type is equivalent to adding 1 to this binary number
#solution is to convert given string to binary representation
#then, convert to decimal representation and add D, before converting back to binary representation
S,D = stdin.readline().split()
D = int(D)
bRep = "".join("0" if S[i] == "A" else "1" for i in range(len(S) - 1, -1, -1))
result = int(bRep,2) + D
ans = reversedBinary(result,len(S))
#reverse string
stdout.write("".join("A" if char == "0" else "B" for char in ans))


