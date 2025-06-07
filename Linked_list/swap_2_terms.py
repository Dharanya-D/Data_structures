class Node:
    def __init__(self, n):
        self.data = n
        self.next = None
        self.prev = None

class DLL:
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

    def get_node_at(self, pos):
        temp = self.head
        count = 1
        while temp and count < pos:
            temp = temp.next
            count += 1
        return temp

    def swap(self, f, b):
        if self.head is None:
            print("List is empty")
            return
        node1 = self.get_node_at(f)
        node2 = self.get_node_at(b)
        if not node1 or not node2:
            print("Position out of range")
            return
        node1.data, node2.data = node2.data, node1.data

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


ob = DLL()
n = int(input())
val = list(map(int, input().split()))
for i in val:
    ob.insert(i)
f = int(input())
b = n - f + 1  
ob.swap(f, b)
ob.display()
