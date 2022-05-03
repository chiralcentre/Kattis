from sys import stdin,stdout

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.back = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # insert new node on front of list
    def push(self,new_node):
        new_node.next = self.head
        if self.head != None:
            self.head.back = new_node
        else:
            self.tail = new_node
        self.head = new_node #move head to point to new node
    # insert node after given node
    def insertAfter(self,prev_node,new_node):
        if prev_node == None:
            print("given previous node cannot be None")
            return
        insertTail = True if prev_node == self.tail else False
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.back = prev_node
        if new_node.next != None:
            new_node.next.back = new_node
        if insertTail:
            self.tail = new_node
    #print contents of linked list, starting from head      
    def listprint(self):
        temp = self.head
        while temp != None:
            stdout.write(temp.value)
            temp = temp.next

for _ in range(int(stdin.readline())):
    string = stdin.readline().strip()
    DLL,curr,operations = DoublyLinkedList(),None,{'<','[',']'}
    for char in string:
        if char not in operations:
            if curr == None: #cursor is at start of DLL
                curr = Node(char)
                DLL.push(curr)
            else:
                DLL.insertAfter(curr,Node(char))
                curr = curr.next
        elif DLL.head != None: #check if list is empty
            if char == '<':
                if curr != None:
                    if curr == DLL.head:
                        DLL.head = curr.next
                        if DLL.head != None:
                            DLL.head.back = None
                        curr = None
                    else:
                        tail = True if curr == DLL.tail else False
                        temp = curr
                        curr = temp.back
                        curr.next = temp.next
                        if curr.next != None: 
                            curr.next.back = curr
                        temp.next,temp.back = None,None #garbage collection
                        if tail:
                            DLL.tail = curr
            elif char == '[':
                curr = None
            else: #']'
                curr = DLL.tail
    DLL.listprint()
    stdout.write('\n')
                
            
