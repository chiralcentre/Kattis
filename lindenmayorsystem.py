from sys import stdin

# let length of starting sequence be L
# code runs in O(L(5^m)) time
n,m = map(int,stdin.readline().split())
rules = {}
for _ in range(n):
    s,e = stdin.readline().strip().split(" -> ")
    rules[s] = list(e)
curr = list(stdin.readline().strip())
for i in range(m):
    new_curr = []
    for letter in curr:
        new_curr.extend(rules.get(letter,[letter]))
    curr = new_curr
print("".join(curr))
