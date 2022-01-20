while True:
    W,L = map(int,input().split())
    if W == L == 0:
        break
    robot_x,robot_y,actual_x,actual_y = 0,0,0,0
    for _ in range(int(input())):
        movement = input().split()
        if movement[0] == 'u':
            robot_y += int(movement[1])
            actual_y = min(actual_y + int(movement[1]),L-1)
        elif movement[0] == 'd':
            robot_y -= int(movement[1])
            actual_y = max(actual_y - int(movement[1]),0)
        elif movement[0] == 'l':
            robot_x -= int(movement[1])
            actual_x = max(actual_x - int(movement[1]),0)
        elif movement[0] == 'r':
            robot_x += int(movement[1])
            actual_x = min(actual_x + int(movement[1]),W-1)
    print(f'Robot thinks {robot_x} {robot_y}')
    print(f'Actually at {actual_x} {actual_y}')
    
        
