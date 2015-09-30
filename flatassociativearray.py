class FlatAssociativeArray:

    def __init__(self, array):
        """Inits from array to histogram"""
        self.data_list = []
        self.keys = []
        if array:
            for item in array:
                if not self.search(item):
                    self.insert(item)
                else:
                    self.update(item)
            self.keys = self.getKeys()

    def insert(self, data):
        """Appends data to end of list,
        updates keys with data

        Params: data - key of thing to add
        str -> ()
        *Should only be called if data not in data_list
        """
        item = (data, 1)
        self.data_list.append(item)
        self.keys = self.getKeys()

    def update(self, data):
        """Increases count of data

        Params: data - key of elem to update
        str -> ()
        * if data in keys, increases count
        """
        index = self.getIndex(data)
        self.data_list[index] = (self.getKey(index), self.getValue(index) + 1)

    def remove(self, data):
        """Removes given tuple

        Params: data - elem to remove
        (str, int) -> ()
        """
        key = data[0]
        index = self.getIndex(key)
        self.data_list.remove(index)

    def search(self, key):
        """Returns (key, val) item given key

        Params: key - key of data to retrive
        str -> (str, int)
        """
        index = self.getIndex(key)
        if index:
            return self.data_list[index]
        return None

    def getIndex(self, key):
        """Returns index of key | O(n)

        Params - key - key of data to retrive
        str -> int
        """
        keys = self.keys
        for i in range(len(keys)):
            if key == keys[i]:
                return i

    def getKey(self, index):
        """Returns key at index

        int -> str
        """
        return self.data_list[index][0]

    def getValue(self, key):
        """Returns value of key (FREQUENCY)

        str -> int
        """
        index = self.getIndex(key)
        if index:
            return self.data_list[index][1]

    def getKeys(self):
        """Returns all keys in data_list

        () -> array
        """
        keys = []
        for item in self.data_list:
            keys.append(item[0])
        return keys

    def __iter__(self):
        """Required for iterable"""
        for item in self.data_list:
            yield item

    def __getitem__(self, index):
        """Required for iterable"""
        return self.search(index)

    def __name__(self):
        """Required for timeit benchmark"""
        return "FlatAssociativeArray"
