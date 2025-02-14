class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  

    def hash_function(self, key):
        return key % self.size  

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None:  
            index = (index + 1) % self.size  
            if index == original_index:
                print("Hash Table is full!")
                return
        
        self.table[index] = (key, value)  

    def search(self, key):
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None:
            print(self.table[index])
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size  
            if index == original_index:
                break
        
        return None  


ht = LinearProbingHashTable(5)
ht.insert(10, "A")
ht.insert(15, "B")  
ht.insert(20, "C")  

print(ht.search(15))  
print(ht.search(25))  
