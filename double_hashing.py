class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return 1 + (key % (self.size - 1))  

    def insert(self, key, value):
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0

        while self.table[index] is not None:
            index = (index + i * step) % self.size
            i += 1
            if i == self.size:
                print("Hash Table is full!")
                return
        
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + i * step) % self.size
            i += 1
            if i == self.size:
                break
        
        return None

# Example Usage
ht = DoubleHashingHashTable(5)
ht.insert(10, "A")
ht.insert(15, "B")
ht.insert(20, "C")

print(ht.search(15)) 
