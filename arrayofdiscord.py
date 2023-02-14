from sys import stdin,stdout

#if all array elements have different lengths, it is impossible to make the list unsorted by changing only one digit
def solve(arr,n):
    for i in range(n - 1):
        #if two elements have the same length, change most significant digit to 0,1 or 9
        if len(arr[i]) == len(arr[i + 1]):
            MSB_A = int(arr[i][0])
            MSB_B = int(arr[i + 1][0])
            if len(arr[i]) == 1:
                if MSB_A == 0:
                    if MSB_B == 9:
                        continue
                    else:
                        arr[i] = "9"
                else:
                    arr[i+1] = "0"
            else:
                if MSB_A == 1:
                    if MSB_B != 9:
                        arr[i] = "9" + arr[i][1:]
                    elif int(arr[i][1:]) <= int(arr[i+1][1:]):
                        continue
                    elif int(arr[i][1:]) > int(arr[i+1][1:]):
                        arr[i + 1] = "1" + arr[i+1][1:]
                #note if MSB_A != 9, replacing MSB_B with 1 ensures that arr[i+1] < arr[i]
                else:
                    arr[i + 1] = "1" + arr[i +1][1:]  
            return " ".join(num for num in arr)    
    return "impossible"

n = int(stdin.readline())
arr = stdin.readline().split()
stdout.write(solve(arr,n))
