def fizzbuzz(M):
    result = []
    for i in range(1,M+1):
        if i%3 and i%5:
            result.append(str(i))
        elif not i%3 and i%5:
            result.append('fizz')
        elif i%3 and not i%5:
            result.append('buzz')
        else: # divisible b5 both 3 and 5
            result.append('fizzbuzz')
    return result

N,M = map(int,input().split())
answer = fizzbuzz(M)
candidate,highest_num_correct = 0,-1
for i in range(1,N+1): #candidate number = i
    counter,output = 0,input().split()
    for j in range(M):
        if output[j] == answer[j]:
            counter += 1
    if counter > highest_num_correct:
        candidate = i
        highest_num_correct = counter
print(candidate)
    
