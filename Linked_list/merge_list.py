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
    
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

ob = LL()
n1 = int(input())
val1 = list(map(int, input().split()))
n2 = int(input())
val2 = list(map(int, input().split()))

i = j = 0
while i < n1 and j < n2:
    if val1[i] < val2[j]:
        ob.insert(val1[i])
        i += 1
    else:
        ob.insert(val2[j])
        j += 1

while i < n1:
    ob.insert(val1[i])
    i += 1
while j < n2:
    ob.insert(val2[j])
    j += 1

ob.display()
