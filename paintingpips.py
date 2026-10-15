N,M = map(int,input().split())
# less pips than number of die, one die will have 0 pips on it
if M < N:
    print(0)
else:
    # spread pips across die as evenly as possible
    q = M // N
    r = M % N
    # r dice get q + 1 pips, N - r dice get q pips
    print(pow(q + 1, r) * pow(q,N - r) / pow(6,N))
