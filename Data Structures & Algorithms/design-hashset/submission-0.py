class MyHashSet:

    def __init__(self):
        self.hashSet = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.hashSet)):
            if self.hashSet[i] == key:
                if i < len(self.hashSet) - 1:
                    self.hashSet = self.hashSet[:i] + self.hashSet[i+1:]
                    return
                else:
                    self.hashSet = self.hashSet[:i]
                    return

    def contains(self, key: int) -> bool:
        for i in range(len(self.hashSet)):
            if self.hashSet[i] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)