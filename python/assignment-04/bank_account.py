class Account:
    def __init__(self, holder, opening_balance=0):
        self.holder = holder
        self.__balance = opening_balance
        self._log = []


    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <=0:
            raise ValueError("deposit amount must be positive")
        self.__balance += amount
        self._log.append({"type":"credit", "amount":amount})
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient Balance")
        self.__balance -= amount
        self._log.append({"type":"debit", "amount":amount})
        return self.__balance


a1 = Account("Prince", 100000)

print(a1.deposit(25000))

try:
    a1.withdraw(200000)
except ValueError as e:
    print("Value Error:", e)


try:
    a1.deposit(-25000)
except ValueError as e:
    print("Value Error:", e)


print(a1.balance)
print(a1._log)