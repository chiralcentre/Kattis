from sys import stdin,stdout

for line in stdin:
    stdout.write("{:.2f}".format(eval(line)) + '\n')
