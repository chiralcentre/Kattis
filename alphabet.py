# check for length of longest increasing subsequence according to alphabet
def longest_length(string,n):
    lst = [1]
    longest = 1
    for i in range(1,n):
        lst.append(1)
        for j in range(i):
            if ord(string[i]) > ord(string[j]) and lst[i] < lst[j] + 1: 
                lst[i] = lst[j] + 1 #number in list reflects position of the character in a potential subsequence
                if lst[i] > longest:
                    longest = lst[i]
    return(longest)      
    
string = input().strip()
n = len(string)
print(26-longest_length(string,n))

            

