from sys import stdin,stdout
from heapq import heappush,heappop,heapify

n,m,k = map(int,stdin.readline().split())
books = []
for i in range(n):
    line = stdin.readline().strip()
    left_index,right_index = line.index('"'),line.rindex('"')
    title = line[left_index+1:right_index]
    t = int(line[right_index+1:])
    if title < "Jane Eyre": #ignore all books lexicographically larger than Jane Eyre
        books.append((title,t))
books.append(("Jane Eyre",k))
#convert list into minimum heap in O(n) time
heapify(books)
#take in the books from friends
friend_books = []
for i in range(m):
    line = stdin.readline().strip()
    left_index,right_index = line.index('"'),line.rindex('"')
    title = line[left_index+1:right_index]
    a = int(line[:left_index]); k = int(line[right_index+1:])
    if title < "Jane Eyre": #ignore all books lexicographically larger than Jane Eyre
        friend_books.append((a,title,k))
#sort by arrival timings in O(m log m) time
friend_books.sort(key = lambda x: x[0], reverse = True)
#the boolean variable read keeps track of whether Jane Eyre has been read 
time,read = 0,False
#O(n log n)
while not read:
    title,t = heappop(books)
    time += t
    if title == "Jane Eyre":
        read = True
    else:
        while friend_books and friend_books[-1][0] <= time: #take in all the books that have been received before the current book has been read
            a,b,k = friend_books.pop()
            heappush(books,(b,k))
stdout.write(f"{time}\n")
            

    


