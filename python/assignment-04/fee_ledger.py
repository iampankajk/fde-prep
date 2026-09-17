class Enrollment:
    def __init__(self, name, code, fee):
        self.code = code
        self.name = name
        self._fee = fee
        self._receipts = []


    @property
    def balance(self):
        rem = self._fee
        for receipt in self._receipts:
            rem -= receipt["amount"]
        return rem

    @property
    def paid(self):
        return self._fee - self.balance

    @property
    def is_settled(self):
        return self.balance == 0


    def make_payment(self, amount, mode):
        if amount <=0:
            raise ValueError("amount must be positive")
        if self.balance < amount:
            raise ValueError("amount must be less or equal to due amount")
        self._receipts.append({"amount":amount, mode:"Upi"})
        return self.balance

    def __str__(self):
        state = "settled" if self.is_settled else f"{self.balance,} due"
        return f"{self.name} {self.code}: Paid ₹{self.paid} of ₹{self._fee} - {state}"

e1 = Enrollment("Pankaj", "FDE", 149000)

e1.make_payment(59750, "UPI")
print(e1.balance)
try:
    e1.make_payment(89250, "UPI")
except ValueError as e:
    print("ValueError:", e)

print(e1)