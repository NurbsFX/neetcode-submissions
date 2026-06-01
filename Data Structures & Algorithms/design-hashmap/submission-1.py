class ListNode:
    def __init__(self, key, value):
        self.val = [key, value]
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashMap = [ListNode(0, 0) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = key % 10**4
        current = self.hashMap[index]
        while current.next:
            if current.next.val[0] == key:
                current.next.val[1] = value
                return
            current = current.next
        current.next = ListNode(key, value)
        return
        

    def get(self, key: int) -> int:
        index = key % 10**4
        current = self.hashMap[index]
        while current.next:
            if current.next.val[0] == key:
                return current.next.val[1]
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        index = key % 10**4
        current = self.hashMap[index]
        while current.next:
            if current.next.val[0] == key:
                current.next = current.next.next
                return
            current = current.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)