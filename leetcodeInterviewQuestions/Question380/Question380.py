class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.arr.append(val)
        self.d[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        temp = self.arr[-1]
        ind = self.d[val]
        self.d[temp] = ind
        self.arr[ind] = temp
        self.arr.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        ind = randint(0, len(self.arr) - 1)
        return self.arr[ind]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()