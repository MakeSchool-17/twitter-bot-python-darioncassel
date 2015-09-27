class FlatAssociativeArray:

    data_list = []
    keys = []

    # inits from array to HISTOGRAM
    def __init__(self, array):
        self.data_list = []
        if array:
            for item in array:
                if not self.search(item):
                    self.insert(item)
                else:
                    self.update(item)
            self.keys = self.getKeys()

    # if data not in self.keys
    def insert(self, data):
        item = (data, 1)
        self.data_list.append(item)
        self.keys = self.getKeys()

    # if data in keys
    def update(self, data):
        index = self.getIndex(data)
        self.data_list[index] = (self.getKey(index), self.getValue(index) + 1)

    # removes given tuple
    def remove(self, data):
        key = data[0]
        index = self.getIndex(key)
        self.data_list.remove(index)

    # returns (key, val) item
    def search(self, key):
        index = self.getIndex(key)
        if index:
            return self.data_list[index]
        return None

    # returns index of key | O(n)
    def getIndex(self, key):
        keys = self.keys
        for i in range(len(keys)):
            if key == keys[i]:
                return i

    # returns key at index
    def getKey(self, index):
        return self.data_list[index][0]

    # returns value of key (FREQUENCY)
    def getValue(self, key):
        index = self.getIndex(key)
        if index:
            return self.data_list[index][1]

    # returns all keys in data_list
    def getKeys(self):
        keys = []
        for item in self.data_list:
            keys.append(item[0])
        return keys

    # required for iterable
    def __iter__(self):
        for item in self.data_list:
            yield item

    # required for iterable
    def __getitem__(self, index):
        return self.search(index)

    # required for timeit benchmark
    def __name__(self):
        return "FlatAssociativeArray"
