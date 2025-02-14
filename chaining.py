class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))  

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:  
            if k == key:
                return v
        return None


ht = ChainingHashTable(5)
ht.insert(10, "A")
ht.insert(15, "B")  
ht.insert(20, "C")  

print(ht.search(15))  
print(ht.search(10))  
