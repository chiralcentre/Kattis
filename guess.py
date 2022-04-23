from sys import exit

#perform binary search
#a correct guess is guaranteed within 10 guesses since 2**10 = 1024 > 1000
low,high = 1,1000
while low <= high:
    mid = (low + high)//2; print(mid)
    response = input().strip()
    if response == "lower":
        high = mid - 1
    elif response == "higher":
        low = mid + 1
    else: #correct
        exit(0)
