class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.maxSize = k
        self.size = 0
        self.recent = self.old = Node(-1)
        self.recent.next, self.recent.prev = self.old, self.old
        self.old.next, self.old.prev = self.recent, self.recent

    def enQueue(self, value: int) -> bool:
        if self.recent.val == -1:
            self.recent.val = self.old.val = value
            self.size += 1
            return True
        if self.size < self.maxSize: 
            newNode = Node(value)
            current = self.recent

            current.next = newNode
            newNode.next = self.old

            newNode.prev = current
            self.old.prev = newNode
            
            self.recent = newNode
            self.size += 1
            return True
        else: 
            return False

    def deQueue(self) -> bool:

        if self.size == 0:
            return False

        if self.size == 1:
            self.recent = self.old = Node(-1)
            self.size -= 1
            return True

        newOld = self.old.next
        newOld.prev = self.recent
        self.recent.next = newOld
        self.old = newOld
        self.size -= 1

        return True

    def Front(self) -> int:
        return self.old.val

    def Rear(self) -> int:
        return self.recent.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxSize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()