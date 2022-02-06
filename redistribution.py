n = int(input())
#offset zero indexing and sort by number of students in each room in ascending order
students = list(map(int,input().split()))
rooms = sorted([(key+1,value) for key,value in enumerate(students)],key = lambda x: x[1])
total_students = sum(students)
# if total students < 2*largest number of students, some students in room with largest number of students will be grading their own scripts
if total_students < 2*rooms[n-1][1]:
    print("impossible")
else:
    order = []
    while rooms:
        index,num = rooms.pop()
        order.append(str(index))
    print(' '.join(order))
    

    
