class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        n = len(self.balance) 
        if account1 <= n and account2 <= n:
            if self.balance[account1-1] - money >= 0:
                self.balance[account1-1] -= money
                self.balance[account2-1] += money
                return True
        return False
        
    def deposit(self, account: int, money: int) -> bool:
        n = len(self.balance)
        if account <= n:
            self.balance[account-1] += money
            return True

    def withdraw(self, account: int, money: int) -> bool:
        n = len(self.balance)
        if account <= n:
            if self.balance[account-1] - money >= 0:
                self.balance[account-1] -= money
                return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)