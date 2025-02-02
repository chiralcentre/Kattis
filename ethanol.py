from sys import stdout

def printHLine(c):
    stdout.write("  ")
    for i in range(c):
        stdout.write("H")
        if i < c - 1:
            stdout.write(" ")
    stdout.write("\n")

def printDLine(c):
    stdout.write("  ")
    for i in range(c):
        stdout.write("|")
        if i < c - 1:
            stdout.write(" ")
    stdout.write("\n")

def printMiddleLine(c):
    stdout.write("H-")
    for i in range(c):
        stdout.write("C-")
    stdout.write("OH\n")
    
c = int(input())
# print first line
printHLine(c)
# print second line
printDLine(c)
# print thhird line
printMiddleLine(c)
# print fourth line
printDLine(c)
# print fifth line
printHLine(c)
