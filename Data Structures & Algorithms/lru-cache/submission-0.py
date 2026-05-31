class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.Qcache = deque()

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.Qcache.remove(key)
            self.Qcache.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.Qcache.remove(key)
            self.Qcache.append(key)
        else: 
            if len(self.cache) >= self.capacity:
                key2remove = self.Qcache.popleft()
                del self.cache[key2remove]
            self.cache[key] = value
            self.Qcache.append(key)