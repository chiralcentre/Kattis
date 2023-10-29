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
            stdout.write(f"{temp.value}")
            if temp.next != None:
                stdout.write(" ")
            temp = temp.next
        stdout.write("\n")

# O(N) approach, only need to check neighbours of those nodes removed
N = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
DLL = DoublyLinkedList()
c = Node(arr[0])
DLL.pushFront(c)
for i in range(1,N):
    DLL.insertAfter(c,Node(arr[i]))
    c = c.next
curr = DLL.head
candidates,seen,removed,ans = [],set(),[],[]
while curr != None:
    if (curr.back != None and curr.back.value > curr.value) or (curr.next != None and curr.next.value > curr.value):
        removed.append(curr)
        if curr.back != None and curr.back not in seen:
            candidates.append(curr.back)
            seen.add(curr.back)
        if curr.next != None and curr.next not in seen:
            candidates.append(curr.next)
            seen.add(curr.next)
    curr = curr.next


while removed:
    ans.append(" ".join(str(node.value) for node in removed))
    for node in removed:
        DLL.remove(node)
    removed = [] # clear removed list
    temp,seen = [],set()
    for cand in candidates:
        if (cand.back != None and cand.back.value > cand.value) or (cand.next != None and cand.next.value > cand.value):
            removed.append(cand)
            if cand.back != None and cand.back not in seen:
                temp.append(cand.back)
                seen.add(cand.back)
            if cand.next != None and cand.next not in seen:
                temp.append(cand.next)
                seen.add(cand.next)
    candidates = temp

stdout.write(f"{len(ans)}\n")
for movement in ans:
    stdout.write(movement)
    stdout.write("\n")
DLL.listprint()
