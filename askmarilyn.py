from random import randint

pos = ["A", "B", "C"]
#Monty hall problem: if bottle is not behind door, change to door unopened
for i in range(1000):
    door = pos[randint(0,2)] #randomise starting location
    print(door)
    chosen,n = input().split()
    if n == "1":
        print(chosen)
    else:
        for d in pos:
            if d != door and d != chosen:
                print(d)
                break
    input() #read in Marilyn's response
        
