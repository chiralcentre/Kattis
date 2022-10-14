from sys import stdin,stdout

S = stdin.readline().strip()
nums = stdin.readline().strip()
message = [S[int(nums[i:i+3]) -1] for i in range(0,len(nums),3)]
stdout.write(''.join(char for char in message))
    
