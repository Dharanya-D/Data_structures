class node:
    def __init__(self,n):
        self.data = n
        self.next = None

class LL():
    def __init__(self):
        self.head = None
    def insert(self,n):
        nn= node(n)
        if self.head is None:
            self.head = nn
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nn
        
    def critical_task(self,pos):
        count = 1
        if self.head is None:
            print("List is empty")
        temp = self.head
        while temp.next is not None and count < pos:
            temp = temp.next
            count+=1
        self.head = temp
        
    def display(self):
        if self.head is None:
            print("List is empty")
        temp =self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
            
ob = LL()
n = int(input())
val = list(map(int,input().split()))
for i in val:
    ob.insert(i)
if n%2 == 0:
    m=(n/2)+1
else:
    m=(n/2)+0.5
    
ob.critical_task(m)
ob.display()
