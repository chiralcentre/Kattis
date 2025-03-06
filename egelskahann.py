from sys import stdout

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.back = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    # insert new node on front of list
    def pushFront(self,new_node):
        new_node.next = self.head
        if self.head != None:
            self.head.back = new_node
        else:
            self.tail = new_node
        self.head = new_node #move head to point to new node
        self.size += 1
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
        self.size += 1
    # remove node
    def remove(self,node):
        if self.head == None or node == None:
            return
        # Case 1: node to be removed is head
        if self.head == node:
            self.head = node.next
        # Case 2: node to be removed is tail
        if self.tail == node:
            self.tail = node.back
        # change prev reference for next node
        if node.next != None:
            node.next.back = node.back
        # change next reference for previous node
        if node.back != None:
            node.back.next = node.next
        # garbage collection
        node.back = None
        node.next = None
        self.size -= 1
        
    #print contents of linked list, starting from head      
    def listprint(self):
        temp = self.head
        # stdout.write("List: ")
        while temp != None:
            stdout.write(f"{temp.value}\n")
            temp = temp.next

# code runs in O(N) time
N = int(input())
DLL = DoublyLinkedList()
DLL.pushFront(Node(0))
curr = DLL.head
for i in range(1,N):
    DLL.insertAfter(curr,Node(i))
    curr = curr.next
curr = DLL.head
while DLL.size > 1:
    for i in range(2):
        prev = curr
        curr = curr.next
        if curr == None:
            curr = DLL.head
    DLL.remove(prev)
print(DLL.head.value + 1)
