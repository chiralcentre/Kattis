from sys import stdin,stdout

def mia(s0,s1,r0,r1):
    highest = {'12','21'}
    doubles = {'11': 1,'22': 2,'33': 3,'44': 4,'55': 5,'66': 6}
    # check if any combination is highest
    if s0 + s1 in highest and r0 + r1 in highest:
        return 'Tie.'
    elif s0 + s1 in highest:
        return 'Player 1 wins.'
    elif r0 + r1 in highest:
        return 'Player 2 wins.' 
    # check for doubles
    if s0 == s1 and r0 == r1:
        return 'Player 1 wins.' if doubles[s0+s1] > doubles[r0+r1] else 'Tie.' if doubles[s0+s1] == doubles[r0+r1] else 'Player 2 wins.'
    elif s0 == s1: #player 2 does not have double
        return 'Player 1 wins.'
    elif r0 == r1: #player 1 does not have double
        return 'Player 2 wins.'
    # remaining rolls are sorted such that highest number comes first
    num1,num2 = int(''.join(sorted([s0,s1],reverse = True))),int(''.join(sorted([r0,r1],reverse = True)))
    return 'Player 1 wins.' if num1 > num2 else 'Tie.' if num1 == num2 else 'Player 2 wins.'
    
for line in stdin:
    s0,s1,r0,r1 = line.split()
    if s0 == '0' and s1 == '0' and r0 == '0' and r1 == '0':
        break
    stdout.write(mia(s0,s1,r0,r1) + '\n')
    
