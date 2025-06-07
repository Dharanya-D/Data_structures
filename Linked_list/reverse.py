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
        
    def reverse(self):
        if self.head is None:
            print("List is empty")
            return
        prev = None 
        temp = self.head
        while temp:
            nxt = temp.next
            temp.next=prev
            prev = temp
            temp = nxt
        self.head = prev     

            
    def display(self):
        if self.head is None:
            print("List is empty")
        temp =self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
ob = LL()
n = int(input())
for i in range(n):
    song = input()
    ob.insert(song)
ob.reverse()    
ob.display()
    
            
            
