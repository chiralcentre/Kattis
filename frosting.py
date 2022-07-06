from sys import stdin,stdout

def concatenate(lst): #O(n)
    return [sum(lst[::3]),sum(lst[1::3]),sum(lst[2::3])]

stdin.readline() #value of n not needed
A,B = list(map(int,stdin.readline().split())),list(map(int,stdin.readline().split()))
#group areas of same colour together
A,B = concatenate(A),concatenate(B)
yellow_area = A[0]*B[1] + A[1]*B[0] + A[2]*B[2] 
pink_area = A[0]*B[2] + A[1]*B[1] + A[2]*B[0]
white_area = A[0]*B[0] + A[1]*B[2] + A[2]*B[1] 
stdout.write(f"{yellow_area} {pink_area} {white_area}")
