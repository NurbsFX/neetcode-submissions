class FileSystem:

    def __init__(self):
        self.store = {}
        

    def createPath(self, path: str, value: int) -> bool:

        if path in self.store:
            return False
        listFolders = path.split('/')[1:]
        if len(listFolders) == 1:
            self.store[path] = value
            return True
        parentPath = "/" + "/".join(listFolders[:-1])
        if parentPath not in self.store:
            return False
        self.store[path] = value
        return True
        

    def get(self, path: str) -> int:
        if path in self.store:
            return self.store[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
