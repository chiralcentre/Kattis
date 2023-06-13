from sys import stdin,stdout
from math import ceil,comb

#Let X denote the number of votes in the remaining votes going to candidate 1
#X ~ Bin(N - M, 1/2)
for _ in range(int(stdin.readline())):
    N,V1,V2,W = map(int,stdin.readline().split())
    w = ceil((N + 1) / 2) #minimum number of people required to win
    r = N - V1 - V2
    if V1 >= w:
        stdout.write("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!\n")
    elif w > r + V1: #impossible to win
        stdout.write("RECOUNT!\n")
    else:
        # get probability by summing over all possibilities
        p = sum(comb(r,i) for i in range(w - V1, N - V1 - V2 + 1))
        p /= pow(2,r)
        stdout.write("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!\n") if 100 * p > W else stdout.write("PATIENCE, EVERYONE!\n")
        
