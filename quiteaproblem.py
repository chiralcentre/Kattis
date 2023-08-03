from sys import stdin,stdout

MAX_N = 100
b = [0 for _ in range(MAX_N)]

def kmpPreprocess(P):
  global b
  i,j = 0,-1
  b[0] = -1
  while i < len(P):
    while j >= 0 and P[i] != P[j]:
      j = b[j]
    i += 1
    j += 1
    b[i] = j

def kmpSearch(T,P):
  global b
  freq = 0
  i,j = 0,0
  while i < len(T):
    while j >= 0 and T[i] != P[j]:
      j = b[j]
    i += 1
    j += 1
    if j == len(P):
      freq += 1
      j = b[j]
  return freq

P = "problem"
kmpPreprocess(P)
for line in stdin:
    res = kmpSearch(line.lower(),P)
    stdout.write("yes\n") if res else stdout.write("no\n")
