class Node:
    def __init__(self, n):
        self.data = n
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, n):
        nn = Node(n)
        if self.head is None:
            self.head = nn
            self.tail = nn
            return
        self.tail.next = nn
        nn.prev = self.tail
        self.tail = nn
        
    def palindrome(self, n):
        if self.head is None:
            print("List is empty")
            return "No"  
        
        temp1 = self.head
        temp2 = self.tail
        count = 0
        
        while temp1 != None and temp2 != None:
            if temp1.data == temp2.data:
                count += 1
            else:
                return "No"
            temp1 = temp1.next
            temp2 = temp2.prev
        
        return "Yes"


ob = DLL()
n = int(input())
val = list(map(int, input().split()))
for i in val:
    ob.insert(i)
print(ob.palindrome(n))
