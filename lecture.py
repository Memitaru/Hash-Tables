class DynamicArray:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity

    def insert(self, index, value):

        if self.count == self.c1apacity:
            self.double_size()
        
        for idx in range(self.count, index, -1):
            self.storage[idx] = self.storage[idx-1]

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        if self.count == self.c1apacity:
            self.double_size()

        self.storage[self.count] = value

        self.count += 1

    def double_size(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.count):
            new_arr[i] = self.storage[i]

        self.storage = new_arr
        
