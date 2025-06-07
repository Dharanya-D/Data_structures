class node:
    def __init__(self,n):
        self.data = n
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
    
    def d_insert_at_end(self,n):
        nn = node(n)
        if self.head is None:
            self.head = nn
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nn
        nn.prev = temp
        
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
            
ob = DLL()
n = int(input())
val = list(map(int,input().split()))
for i in val:
    ob.d_insert_at_end(i)
    
ob.display()
