class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.count = 1
        while self.stack and self.stack[-1][0] <= price:
            self.count += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price,self.count])
        return self.count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)