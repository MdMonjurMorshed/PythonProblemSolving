class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # get the next element of current 
            current.next = prev  # that means now current indicates the prev value
            prev = current  # now cheng the prev value to move forward
            current = next_node  # change the currnet value to find the next item of it
        self.head = prev  # change the head of the linked list


ll = LinkedList() 
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print("Original List:")
ll.print_list()

ll.reverse()

print("Reversed List:")
ll.print_list()
