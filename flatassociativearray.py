class FlatAssociativeArray:

    data_list = []
    keys = []

    def __init__(self, array):
        self.data_list = []
        if array:
            for item in array:
                if not self.search(item):
                    self.insert(item)
                else:
                    self.update(item)
            self.keys = self.getKeys()

    def insert(self, data):
        if data not in self.keys:
            item = [data, 1]
            self.data_list.append(item)
            self.keys = self.getKeys()

    def update(self, data):
        keys = self.keys
        if data in keys:
            index = self.indexKey(data)
            self.data_list[index][1] = self.data_list[index] + 1

    def search(self, item):
        index = self.indexKey(item)
        if index:
            return self.data_list[index]
        return None

    def indexKey(self, item):
        keys = self.keys
        for i in range(len(keys)):
            if item == keys[i]:
                return i

    def getKeys(self):
        keys = []
        for item in self.data_list:
            keys.append(item[0])
        return keys
