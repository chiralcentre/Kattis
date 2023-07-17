from sys import stdin,stdout

def convertToMin(t):
    h,m = map(int,t.split(":"))
    return h * 60 + m

for line in stdin:
    line = line.split()
    ans = line[0:3]
    elapsed = convertToMin(line[4]) - convertToMin(line[3])
    ans.append(str(elapsed // 60))
    ans.append("hours")
    ans.append(str(elapsed % 60))
    ans.append("minutes")
    stdout.write(" ".join(s for s in ans))
    stdout.write("\n")
