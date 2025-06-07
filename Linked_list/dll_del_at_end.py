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
        
    def d_del_at_end(self):
        if self.head.next is None:
            self.head = None
            print("List is empty")
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None
       
    def display(self):
        if self.head is None:
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
ob.d_del_at_end()    
ob.display()
