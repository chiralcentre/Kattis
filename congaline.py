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
            stdout.write(f"{temp.value}\n")
            temp = temp.next

N,Q = map(int,stdin.readline().split())
pairings,mappings,DLL = {},{},DoublyLinkedList()
curr = None
for i in range(N):
    u,v = stdin.readline().split()
    a,b = Node(u),Node(v)
    if curr == None:
        curr = a
        DLL.pushFront(curr)
    else:
        DLL.insertAfter(curr,a)
        curr = curr.next
    DLL.insertAfter(curr,b)
    curr = curr.next
    pairings[u],pairings[v] = v,u
    mappings[u],mappings[v] = a,b # map each name to their node
        
instructions = stdin.readline().strip()
curr = DLL.head
for char in instructions:
    if char == "F":
        curr = curr.back
    elif char == "B":
        curr = curr.next
    elif char == "R":
        moved = curr
        if curr.next != None:
            curr = curr.next
        else:
            curr = DLL.head # pass to front of line
        DLL.remove(moved)
        DLL.insertAfter(DLL.tail,moved)
    elif char == "C":
        moved = curr
        u = moved.value
        if curr.next != None:
            curr = curr.next
        else:
            curr = DLL.head # pass to front of line
        DLL.remove(moved)
        DLL.insertAfter(mappings[pairings[u]],moved)
    else: # P type, shout name into mike
        stdout.write(f"{pairings[curr.value]}\n")
stdout.write("\n") # empty line
DLL.listprint()
