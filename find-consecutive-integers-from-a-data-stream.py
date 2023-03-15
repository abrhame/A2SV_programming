class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = [0]
        self.value = value
        self.k = k
        self.count = 0
    def consec(self, num: int) -> bool:
        self.stream = [num]
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        if self.count == self.k:
            self.count -= 1
            return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)