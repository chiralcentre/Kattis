#Compressed files can be of lengths 0,...,b
#2**b unqiue files of length b,2*(b-1) of length b - 1 etc
#Sum = 2**(b+1)-1
N,b = map(int,input().split())
print("yes") if (2**(b+1) - 1 >= N) else print("no")
