class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        i = 1
        
        while self.table[index] is not None:
            index = (index + i**2) % self.size  
            i += 1
            if i == self.size:  
                print("Hash Table is full!")
                return
        
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        i = 1
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + i**2) % self.size
            i += 1
            if i == self.size:
                break
        
        return None


ht = QuadraticProbingHashTable(5)
ht.insert(10, "A")
ht.insert(15, "B")
ht.insert(20, "C")

print(ht.search(15))  
