class StringIterator:

    def __init__(self, compressedString: str):
        self.listOfChar = deque()
        numbers = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        i, n = 0, len(compressedString)
        while i < n:
            letter = compressedString[i]
            i += 1
            j = i 
            while j < n and compressedString[j].isdigit():
                j += 1
            number = int(compressedString[i:j])
            self.listOfChar.append([letter, number])
            i = j


    def next(self) -> str:
        nextString = self.listOfChar[0][0]
        if self.listOfChar[0][1] > 1:
            self.listOfChar[0][1] -= 1
        else:
            self.listOfChar.popleft()
        return nextString

    def hasNext(self) -> bool:
        return len(self.listOfChar) != 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
