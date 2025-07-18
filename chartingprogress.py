from sys import stdin,stdout

def print_logs(logs):
    curr = 0
    for i in range(len(logs) - 1, -1, -1):
        runs = 0
        for j in range(len(logs[i])):
            if logs[i][j] == "*":
                runs += 1
                logs[i][j] = "."
        for j in range(curr, curr + runs):
            logs[i][j] = "*"
        curr += runs
    stdout.write("\n".join("".join(row) for row in logs))
    stdout.write("\n")
    
logs = []
for line in stdin:
    line = list(line.strip())
    if line == []:
        print_logs(logs)
        stdout.write("\n")
        logs = []
    else:
        logs.append(line)
if logs:
    print_logs(logs)
    
