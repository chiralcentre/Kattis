from sys import stdin,stdout

n = int(stdin.readline())
cards = list(map(int,stdin.readline().split()))
stack = [cards[0]]
# remove cards from left to right
for i in range(1,n):
    if stack and not (stack[-1]+cards[i])%2:
        stack.pop()
    else:
        stack.append(cards[i])
stdout.write(str(len(stack))+'\n')
