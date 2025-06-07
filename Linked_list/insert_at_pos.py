class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def insert_at_pos(self, pos, data):
        nn = Node(data)
        if pos == 1:
            nn.next = self.head
            self.head = nn
            return
        temp = self.head
        count = 1
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1
        if temp is None:
            print("Position out of range")
            return
        nn.next = temp.next
        temp.next = nn

    def insert_end(self, data):
        nn = Node(data)
        if self.head is None:
            self.head = nn
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = nn

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

ob = LL()
n = int(input())
val = list(map(int, input().split()))
for i in val:
    ob.insert_end(i)

p = int(input())
m = int(input())

ob.insert_at_pos(p, m)
ob.display()
