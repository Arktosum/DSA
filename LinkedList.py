class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,data):
        node = Node(data)
        temp = self.head
        if not temp:
            self.head = node
        else:
            while(temp.next):
                temp = temp.next
            temp.next = node
    def insert_at_head(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_index(self,data,index):
        node = Node(data)
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        node.next = temp.next
        temp.next = node

    def print_ll(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll.insert_at_head(5)
ll.insert_at_head(2)
ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_head(4)
ll.insert_at_index(4,3)
ll.print_ll()
