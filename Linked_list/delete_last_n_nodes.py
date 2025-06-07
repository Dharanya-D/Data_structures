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
        while temp.next:
            temp = temp.next
        temp.next = nn

    def delete_last_n_nodes(self, pos):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        if pos >= count:
            self.head = None
            return
        current = self.head
        for _ in range(count - pos - 1):
            current = current.next
        current.next = None

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

obj = LL()
n = int(input())
a = list(map(int, input().split()))
for i in a:
    obj.insert_node(i)
pos = int(input())

obj.delete_last_n_nodes(pos)
obj.display()
