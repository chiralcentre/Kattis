from sys import stdin,stdout

def leftbeehind(x,y):
    if y + x == 13:
        return 'Never speak again.'
    return 'Left beehind.' if y > x else 'Undecided.' if y == x else 'To the convention.'

for line in stdin:
    x,y = map(int,line.split())
    if x == 0 and y == 0:
        break
    stdout.write(leftbeehind(x,y)+'\n')
