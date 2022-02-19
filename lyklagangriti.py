class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.back = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    # insert new node on front of list
    def push(self,new_node):
        new_node.next = self.head
        if self.head != None:
            self.head.back = new_node
        self.head = new_node #move head to point to new node
    # insert node after given node
    def insertAfter(self,prev_node,new_node):
        if prev_node == None:
            print("given previous node cannot be None")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.back = prev_node
        if new_node.next != None:
            new_node.next.back = new_node
    #print contents of linked list, starting from head      
    def listprint(self):
        temp = self.head
        while temp != None:
            print(temp.value,end='')
            temp = temp.next
            
line = input().strip()
keys,curr,DLL = {'L','R','B'},None,DoublyLinkedList()
for char in line:
    if char not in keys:
        if curr == None: #cursor is at start of DLL
            curr = Node(char)
            DLL.push(curr)
        else:
            DLL.insertAfter(curr,Node(char))
            curr = curr.next
    else:
        if char == 'L':
            curr = curr.back
        elif char == 'R':
            curr = curr.next if curr != None else DLL.head   
        else: #backward key
            if curr == DLL.head:
                temp = curr
                DLL.head = temp.next
                if DLL.head != None:
                    DLL.head.back = None
                curr = None
            else:
                temp = curr
                curr = temp.back
                curr.next = temp.next
                if curr.next != None: 
                    curr.next.back = curr
                temp.next,temp.back = None,None #garbage collection
DLL.listprint()

