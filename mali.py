from sys import stdin,stdout

# 1 <= A,B <= 100
A,B = [0 for _ in range(101)],[0 for _ in range(101)]
tempA,tempB = [0 for _ in range(101)],[0 for _ in range(101)]
for i in range(int(stdin.readline())): #O(N)
    a,b = map(int,stdin.readline().split())
    A[a] += 1; B[b] += 1
    for j in range(101): #101 iterations
        tempA[j],tempB[j] = A[j],B[j] #tempA and tempB stores the frequencies of each number for each round
    Amax,Bmin,sms = 100,1,0 #sms stands for smallest maximal sum
    # a greedy approach is taken where largest value in sequence A is always paired with smallest value in sequence B
    while Amax > 0 and Bmin < 100: #maximum 200 iterations
        # find largest value in A
        while Amax > 0 and tempA[Amax] == 0:
            Amax -= 1
        # find smallest value in B
        while Bmin < 101 and tempB[Bmin] == 0:
            Bmin += 1
        # exceed limits
        if Amax == 0 or Bmin == 101:
            break
        # higher maximal sum is found
        if Amax + Bmin > sms:
            sms = Amax + Bmin
        # remove pairs once formed
        if tempA[Amax] > tempB[Bmin]:
            tempA[Amax] -= tempB[Bmin]
            tempB[Bmin] = 0
        else:
            tempB[Bmin] -= tempA[Amax]
            tempA[Amax] = 0
    stdout.write(f"{sms}\n")
