class node:
    def __init__(self,n):
        self.data = n
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        
    def insert_at_end(self,n):
        nn = node(n)
        if self.head is None:
            self.head = nn
            return 
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = nn
        temp=nn
    def display(self):
        if self.head is None:
            print("The list is empty")
            return 
        temp = self.head
        while temp is not None:
            print(temp.data, end= " ")
            temp = temp.next
            
ob=LL()
n = int (input())
val = list(map(int,input().split()))
for i in val:
    ob.insert_at_end(i)
ob.display()
    
