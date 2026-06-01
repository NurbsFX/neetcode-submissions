class MovingAverage:

    def __init__(self, size: int):
        self.window = size
        self.numbers = []

    def next(self, val: int) -> float:
        self.numbers.append(val)
        n = len(self.numbers)
        if n < self.window: 
            return sum(self.numbers)/n
        print(self.numbers[n-self.window:])
        return sum(self.numbers[n-self.window:])/self.window


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
