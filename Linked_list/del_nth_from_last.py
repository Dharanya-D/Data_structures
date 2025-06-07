class node:
    def __init__(self,n):
        self.data = n
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
    
    def insert(self,n):
        nn = node(n)
        if self.head is None:
            self.head = nn
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nn
    
    def del_nth_from_last(self,pos):
        if self.head is None:
            print("List is empty")
            return 
        count = 1
        temp = self.head
        if pos == 0:
            self.head = self.head.next
            return 
        while temp.next is not None and count<pos:
            temp = temp.next
            count+=1
        if temp.next:
            temp.next= temp.next.next
        else:
            return
        
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

ob = LL()
n = int(input())
val = list(map(int,input().split()))
for i in val:
    ob.insert(i)
t = int(input())
pos = n-t
if pos<n and pos >= 0:
    ob.del_nth_from_last(pos)
    
else:
    print("Position out of range")
ob.display()

        
