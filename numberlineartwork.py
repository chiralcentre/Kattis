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
    def pushFront(self,new_node):
        new_node.next = self.head
        if self.head != None:
            self.head.back = new_node
        else:
            self.tail = new_node
        self.head = new_node #move head to point to new node
    #insert node before given node
    def insertBefore(self, next_node, new_node):
        if next_node == None:
            print("given next node cannot be None")
            return
        insertHead = True if next_node == self.head else False
        new_node.back = next_node.back
        new_node.next = next_node
        next_node.back = new_node
        if new_node.back != None:
            new_node.back.next = new_node
        if insertHead:
            self.head = new_node
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
        
    #print contents of linked list, starting from head      
    def listprint(self):
        temp = self.head
        # stdout.write("List: ")
        while temp != None:
            stdout.write(f"{temp.value}")
            if temp.next != None:
                stdout.write(" ")
            temp = temp.next
        stdout.write("\n")

n,m = map(int,stdin.readline().split())
arms = [None for _ in range(n)]
initial = stdin.readline().strip().split()
DLL = DoublyLinkedList()
for i in range(n - 1, -1, -1):
    DLL.pushFront(Node(initial[i]))
    arms[i] = DLL.head
for _ in range(m):
    q,w = stdin.readline().split()
    q = int(q)
    if w == "L":
        arms[q] = arms[q].back
    elif w == "R":
        arms[q] = arms[q].next
    else:
        new_node = Node(w)
        DLL.insertBefore(arms[q], new_node)
        arms[q] = new_node
DLL.listprint()
