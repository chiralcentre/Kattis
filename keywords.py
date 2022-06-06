from sys import stdin,stdout

n = int(stdin.readline())
keywords = set()
for i in range(n):
    string = stdin.readline().strip()
    string = string.replace('-',' ')
    keywords.add(string.lower())
stdout.write(str(len(keywords)))
