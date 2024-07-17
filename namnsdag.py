from sys import stdin

def checkIfThereIsOnlyOneDiff(s1,s2):
    if len(s1) != len(s2):
        return False
    return sum(s1[i] != s2[i] for i in range(len(s1))) == 1
        

def solve():
    friend = stdin.readline().strip()
    N = int(stdin.readline())
    for i in range(N):
        name = stdin.readline().strip()
        if checkIfThereIsOnlyOneDiff(friend,name):
            return i + 1
    return N

if __name__ == "__main__":
    print(solve())
