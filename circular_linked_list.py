class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            print("set first node")
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            
            print("i am in while",temp.next)
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head  # Making it circular

    def traverse(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print(self.head.data)

# Example usage
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.traverse()
