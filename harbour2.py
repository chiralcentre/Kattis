from sys import stdin

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

    def pushBack(self,new_node):
        # empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.back = self.tail
            self.tail.next = new_node
            self.tail = new_node

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

# overall code runs in O(n) time
n,a,b = map(int,stdin.readline().split())
mappings = [None for _ in range(n + 1)]
s1,s2 = list(map(int,stdin.readline().split())),list(map(int,stdin.readline().split()))
# use a single doubly linked list to represent the two stacks
# the DLL will be made of stack 1 written out bottom-to-top, and stack 2 written out top-to-bottom, concatenated 
frontier = DoublyLinkedList()
for t in s1:
    node = Node(t)
    mappings[t] = node
    frontier.pushBack(node)
for i in range(b - 1, -1, -1):
    node = Node(s2[i])
    mappings[s2[i]] = node
    frontier.pushBack(node)

# remove every node in ascending order
# in each iteration, check if neighbours contain node 0
# this works because when a node is removed, the boundary between the two stacks is moved there
ans = 0
for i in range(1,n + 1):
    to_remove = mappings[i]
    if (to_remove.back != None and to_remove.back.value == 0) or (to_remove.next != None and to_remove.next.value == 0):
        ans += 1
    frontier.remove(to_remove)
print(ans)
