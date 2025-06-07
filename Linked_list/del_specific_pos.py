class Node:
    def __init__(self, n):
        self.data = n
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def insert_node(self, n):
        nn = Node(n)
        if self.head is None:
            self.head = nn
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = nn

    def del_specific_pos(self, pos):
        if self.head is None:
            print("list is empty")
            return
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        count = 1
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1
        if temp is None or temp.next is None:
            print("Position out of range")
            return
        temp.next = temp.next.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


ob = LL()
n = int(input())
if n > 0:
    val = list(map(int, input().split()))
    for i in val:
        ob.insert_node(i)
    pos = int(input())
    ob.del_specific_pos(pos)
ob.display()

