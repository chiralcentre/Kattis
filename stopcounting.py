from sys import stdin,stdout

N = int(stdin.readline())
cards = list(map(int,stdin.readline().split()))
# The problem can be rephrased as given an array of integers, find the maximum attainable average after deleting some subarray
# The maximum average will always be prefix or suffix of array. Try all possible combinations in O(N) time.
highest_average = 0 #highest_average must be at least 0
# iterate through prefixes
average1,elems,end1 = 0,0,0
while end1 <= N - 1:
    average1 = (average1*elems + cards[end1])/(elems+1)
    end1 += 1; elems += 1
    highest_average = max(average1,highest_average)
# iterate through suffixes
average2,elems,end2 = 0,0,N-1
while end2 >= 0:
    average2 = (average2*elems + cards[end2])/(elems+1)
    end2 -= 1; elems += 1
    highest_average = max(average2,highest_average)
        
stdout.write(f'{highest_average}\n')
    
