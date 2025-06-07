class node:
    def __init__(self,n):
        self.data=n
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def insert_node(self,n):
        nn=node(n)
        temp=self.head
        if self.head is None:
            self.head=nn
            return
        while temp.next is not None:
            temp=temp.next
        temp.next=nn
    def delete_node(self,pos):
        if self.head is None:
            return
        for i in range(pos):
            if self.head is None:
                break
            self.head=self.head.next
    def display(self):
        temp=self.head
        if self.head is None:
            print("List is empty")
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
obj=LL()
n=int(input())
a=list(map(int,input().split()))
for i in a:
    obj.insert_node(i)
pos=int(input())
obj.delete_node(pos)
obj.display()
