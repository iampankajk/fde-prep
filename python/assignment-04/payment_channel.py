from abc import ABC, abstractmethod

class PaymentChannel(ABC):
    @abstractmethod
    def label(self):
        pass

    @abstractmethod
    def collect(self, amount):
        pass


class UpiChannel(PaymentChannel):
    def label(self):
        return "UPI"

    def collect(self, amount):
        return amount <= 100000

class NeftChannel(PaymentChannel):
    def __init__(self, bank_name):
        self.bank_name = bank_name

    def label(self):
        return f"Neft/{self.bank_name}"

    def collect(self, amount):
        return True

class CardChannel(PaymentChannel):
    def __init__(self, last_four):
        self.last_four = last_four

    def label(self):
        return "Card"

    def collect(self, amount):
        return amount <= 50000


def collect_installments(channels, due, amount):
    for channel in channels:
        if channel.collect(amount):
            due -= amount 
        print(f"{channel.label()} -> still due: Rs {due:,}")
    return due


channels = [
    UpiChannel(),
    NeftChannel("HDFC Bank"),
    CardChannel("1234")
]

due = 149000
balance = collect_installments(channels, due, 25000)


print(f"Final balance: Rs {balance:,}")


print("\nTrying Rs 60,000 on card:")

card = CardChannel("1234")
if card.collect(60000):
    print(f"{card.label()} -> payment accepted")
else:
    print(f"{card.label()} -> payment declined")


print("\nTrying to instantiate PaymentChannel:")

try:
    channel = PaymentChannel()
except TypeError as e:
    print("TypeError:", e)