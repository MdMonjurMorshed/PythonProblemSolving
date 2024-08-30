class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def enqueue(self,data):

        new_node = Node(data)
        new_node.next = None
        print(new_node)
        if not new_node:
            print("stack overflow")
            return
        if self.head is None:
            print('first')
            self.head = self.tail = new_node
        else:
            print('another node')
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):


        if self.head is None:
            print("queue underflow")
            return
        else:
            
            temp = self.head
            self.head = self.head.next
            print(self.head)
            del temp
    def front(self):
        if not self.is_empty():
            
            return self.head.data  
        else:
            return 
        
    def last(self):
        if not self.is_empty():
            return self.tail.data
        else:
            return
 

        


q = Queue()
q.enqueue(4)        
q.enqueue(5)        
q.enqueue(6)
q.enqueue(7)
q.dequeue()
q.dequeue()
print(q.front())
print(q.last())