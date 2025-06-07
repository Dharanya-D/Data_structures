class Node:
    def __init__(self, n):
        self.data = n
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def insert(self, n):
        nn = Node(n)
        if self.head is None:
            self.head = nn
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nn
        nn.prev = temp  

    def swap_pairs(self):
        temp = self.head
        while temp and temp.next:
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

ob = LL()
n = int(input())
val = list(map(int, input().split()))
for i in val:
    ob.insert(i)

ob.swap_pairs()
ob.display()
