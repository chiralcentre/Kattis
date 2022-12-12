from sys import stdin,stdout

#note that rearranging columns does not change result, so we can assume first row is sorted in descending order
#similarly, second row icons can be assumed to be sorted in descending order.
N = int(stdin.readline())
icons = [int(stdin.readline()) for _ in range(2*N)]
prefixSum,evenSum = [0 for _ in range(2*N+1)],[0 for _ in range(2*N+2)]
#O(N)
for i in range(2*N):
    prefixSum[i+1] = prefixSum[i] + icons[i]
    evenSum[i+2] = evenSum[i] + icons[i]
#O(N)
lowest = 2**64
for i in range(1,N+1):
    lowest = min(lowest, (icons[0] + icons[i])*(evenSum[2*N] - evenSum[2*i] + prefixSum[i]))
stdout.write(f"{lowest}")

