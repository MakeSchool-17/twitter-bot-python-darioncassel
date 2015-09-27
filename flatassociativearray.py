class FlatAssociativeArray:

    data_list = []

    def __init__(self, array):
        self.data_list = []
        if array:
            for item in array:
                if not self.search(item):
                    self.insert(item)
                else:
                    self.update(item)

    def insert(self, data):
        keys = self.getKeys()
        if data not in keys:
            item = [data, 1]
            self.data_list.append(item)

    def update(self, data):
        keys = self.getKeys()
        if data in keys:
            index = self.indexKey(data)
            self.data_list[index][1] = self.data_list[index] + 1

    def search(self, item):
        index = self.indexKey(item)
        if index:
            return self.data_list[index]
        return None

    def getKeys(self):
        keys = []
        for item in self.data_list:
            keys.append(item[0])
        return keys

    def indexKey(self, item):
        keys = self.getKeys()
        for i in range(len(keys)):
            if item == keys[i]:
                return i
