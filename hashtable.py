class HashTable:

    keys = []
    vals = []
    length = 0

    def __init__(self, array):
        self.length = len(array)
        self.vals = [None] * self.length
        for key in array:
            if self.get(key):
                self.update(key, self.get(key)+1)
            else:
                self.set(key, 1)

    def get(self, key):
        index = self.index(key)
        if index < len(self.vals):
            return self.vals[index]

    def set(self, key, val):
        index = self.index(key)
        self.vals[index] = val
        self.keys.append(key)

    def update(self, key, val):
        self.set(key, val)

    def getKeys(self):
        return self.keys()

    def getVals(self):
        return self.vals()

    # Generates array index from key
    # params: length of key array, key string
    # (int, str) -> int
    def index(self, key):
        return self.hash_func(key) % self.length

    def hash_func(self, key):
        sum = 0
        if len(key) > 1:
            chars = key.split("")
            for char in chars:
                sum += ord(char)
        else:
            sum += ord(key)
        return sum
