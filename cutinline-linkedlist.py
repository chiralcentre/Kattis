class Person():
    def __init__(self,value = None):
        self.value = value
        self.nextvalue = None

class LinkedList():
    def __init__(self):
        self.headvalue = None
    def listprint(self):
        temp = self.headvalue
        while temp != None:
            print(temp.value)
            temp = temp.nextvalue
    def insert(self,new,original):
        temp = self.headvalue
        if temp.value != original:
            while temp.nextvalue.value != original:
                temp = temp.nextvalue
            placeholder = temp.nextvalue
            temp.nextvalue = Person(new)
            temp.nextvalue.nextvalue = placeholder
        else:
            self.headvalue = Person(new)
            self.headvalue.nextvalue = temp
    def remove(self,name):
        temp = self.headvalue
        if temp.value != name:
            while temp.nextvalue.value != name:
                temp = temp.nextvalue
            temp.nextvalue = temp.nextvalue.nextvalue
        else:
            self.headvalue = self.headvalue.nextvalue
        
        

queue = LinkedList()
names = [Person(input().strip()) for i in range(int(input()))]
for person in names:
    if queue.headvalue == None:
        queue.headvalue = person
    else:
        temp = queue.headvalue
        while temp.nextvalue != None:
            temp = temp.nextvalue
        temp.nextvalue = person

for j in range(int(input())):
    event = input().split()
    if event[0] == 'cut':
        queue.insert(event[1],event[2])
    elif event[0] == 'leave':
        queue.remove(event[1])

queue.listprint()
        
