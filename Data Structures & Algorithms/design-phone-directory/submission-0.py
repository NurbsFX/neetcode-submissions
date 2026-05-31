class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.phoneNumbers = deque([i for i in range(maxNumbers)])
        self.dicPhoneNumbers = set(self.phoneNumbers)
        self.index = 0
        

    def get(self) -> int:
        if len(self.phoneNumbers) == 0 or self.index == len(self.phoneNumbers):
            return -1
        else: 
            phoneNumber =self.phoneNumbers[self.index]
            self.index += 1
            self.dicPhoneNumbers.discard(phoneNumber)
            return phoneNumber

            
    def check(self, number: int) -> bool:
        return number in self.dicPhoneNumbers
        

    def release(self, number: int) -> None:
        self.phoneNumbers.append(number)
        self.dicPhoneNumbers.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
