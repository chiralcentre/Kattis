# start with initial coordinates
# fix y coordinate and vary x coordinate
# repeat the same for y coordinate
# hardcode search path

x = -1
def find_x():
    global x
    print("3 3 .")
    print("6 3 ?")
    x = 6
    res = input().strip()
    if res == "Closer":
        print("8 3 ?")
        x = 8
        res = input().strip()
        if res == "Closer":
            print("9 3 ?")
            x = 9
            res = input().strip()
            if res == "Closer":
                return 9
            elif res == "Farther":
                return 8
            else:
                raise Exception("Not supposed to happen")
        elif res == "Farther":
            print("4 3 ?")
            x = 4
            res = input().strip()
            if res == "Closer":
                return 5
            elif res == "Farther":
                raise Exception("Not supposed to happen")
            else:
                return 6
        else:
            return 7
    elif res == "Farther":
        print("0 3 ?")
        x = 0
        res = input().strip()
        if res == "Closer":
            print("2 3 ?")
            x = 2
            res = input().strip()
            if res == "Closer":
                return 2
            elif res == "Farther":
                return 0
            else:
                return 1
        elif res == "Farther":
            return 4
        else:
            return 3

def find_y():
    global x
    print(f"{x} 6 ?")
    res = input().strip()
    if res == "Closer":
        print(f"{x} 8 ?")
        res = input().strip()
        if res == "Closer":
            print(f"{x} 9 ?")
            res = input().strip()
            if res == "Closer":
                return 9
            elif res == "Farther":
                return 8
            else:
                raise Exception("Not supposed to happen")
        elif res == "Farther":
            print(f"{x} 4 ?")
            res = input().strip()
            if res == "Closer":
                return 5
            elif res == "Farther":
                raise Exception("Not supposed to happen")
            else:
                return 6
        else:
            return 7
    elif res == "Farther":
        print(f"{x} 0 ?")
        res = input().strip()
        if res == "Closer":
            print(f"{x} 2 ?")
            res = input().strip()
            if res == "Closer":
                return 2
            elif res == "Farther":
                return 0
            else:
                return 1
        elif res == "Farther":
            return 4
        else:
            return 3

print(f"{find_x()} {find_y()} !")
