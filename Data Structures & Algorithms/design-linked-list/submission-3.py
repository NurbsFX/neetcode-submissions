class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        current = self.head
        i = 0
        while i != index and current.next:
            current = current.next
            i += 1
        if i < index or not current: 
            return -1 
        else:
            return current.val

    def addAtHead(self, val: int) -> None:
        currentHead = self.head
        self.head = Node(val)
        self.head.next = currentHead
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.head = Node(val)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index > self.length:
            return
        
        current = self.head
        i = 0

        while i < index - 1:
            current = current.next
            i += 1
        newNode = Node(val)
        newNode.next = current.next
        current.next = newNode
        self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        current = self.head
        i = 0

        while i < index - 1:
            current = current.next
            i += 1
        if current.next is not None:
            current.next = current.next.next
            return
        else:
            return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)