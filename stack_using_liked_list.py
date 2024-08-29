class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        
        return self.head is None       
    def push(self,data):

        

        new_node = Node(data)
        if not new_node:
            print("stack overflow")
            return
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("stack underflow")

        else:
            temp = self.head
            self.head  = self.head.next
            del temp   
    def top(self):
        if  not  self.is_empty():
            return self.head.data
            
        else:
            print("stack is empty")
            return
            
                    

st = Stack()
st.push(4)
st.push(5)
st.push(6)
st.push(7)
st.pop()
st.pop()
st.pop()
st.pop()

print(st.top())
