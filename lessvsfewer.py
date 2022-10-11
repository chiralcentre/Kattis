from sys import stdin,stdout

#1 for c, 0 for m, 2 for both
startToNoun = {"number": 1, "amount": 0, "most": 2, "fewest": 1,
              "least": 0, "more": 2, "fewer": 1, "less": 0,
              "many": 1, "much": 0, "few": 1, "little": 0}
n,p = map(int,stdin.readline().split())
wordType = {}
for _ in range(n):
    key,value = stdin.readline().split()
    wordType[key] = 1 if value == "c" else 0
for _ in range(p):
    line = stdin.readline().split()
    stdout.write("Correct!\n") if startToNoun[line[0]] == 2 or startToNoun[line[0]] == wordType[line[-1]] else stdout.write("Not on my watch!\n")
