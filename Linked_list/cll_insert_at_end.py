class node:
    def __init__(self,n):
        self.data = n
        self.next = None
class CLL:
    def __init__(self):
        self.head = None
    
    def c_insert_at_end(self,n):
        nn = node(n)
        if self.head is None:
            self.head = nn
            nn.next = self.head
        temp = self.head     
        while temp.next is not self.head:
            temp = temp.next
        temp.next = nn
        nn.next = self.head
        
    def display(self):
        if self.head is None:
            print("List is empty")
        temp = self.head
        while True:
            print(temp.data,end=" ")
            if temp.next is self.head:
                break
            temp=temp.next
            
ob = CLL()
n = int(input())
val = list(map(int,input().split()))
for i in val:
    ob.c_insert_at_end(i)
ob.display()
