from sys import stdin,stdout

case = 0
while True:
    N = int(stdin.readline())
    if N == 0:
        break
    if case > 0:
        stdout.write("\n") #new line between test cases
    case += 1
    #pile2 is used to store the plates in stack form (LIFO)
    #pile1 is a stack; items placed in it to be removed first were placed into pile2 first, effectively FIFO
    pile1,pile2 = [],[]
    for _ in range(N):
        command,num = stdin.readline().split()
        if command == "DROP":
            pile2.append(int(num))
            stdout.write(f"DROP 2 {int(num)}\n")
        else: #take command
            # take from pile1 if its not empty
            counter,taken = 0,0
            while pile1:
                a = pile1.pop()
                if taken + a <= int(num):
                    taken += a
                else: #enough plates are taken
                    diff = a + taken - int(num)
                    pile1.append(diff)
                    taken = int(num)
                    break
            if taken > 0:
                stdout.write(f"TAKE 1 {taken}\n")
            temp = taken #temp keeps track of number of plates taken from pile1
            if taken < int(num): #there is no need to move if enough plates can be taken from pile1
                # move all plates from pile2 onto pile1, reversing order
                while pile2:
                    counter += pile2[-1]
                    pile1.append(pile2.pop())
                if counter > 0: #a move was made
                    stdout.write(f"MOVE 2->1 {counter}\n")
                # fill in remaining plates
                while taken < int(num):
                    a = pile1.pop()
                    if taken + a <= int(num):
                        taken += a
                    else: #enough plates are taken
                        diff = a + taken - int(num)
                        pile1.append(diff)
                        taken = int(num)
                        break
                if taken - temp > 0:
                    stdout.write(f"TAKE 1 {taken - temp}\n")

