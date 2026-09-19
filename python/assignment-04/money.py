class Money:
    def __init__(self, rupees):
        if not isinstance(rupees, int) or isinstance(rupees, bool):
            raise TypeError("Money must store whole rupees as an integer")

        self.rupees = rupees


    def __repr__(self):
        return f"Money: {self.rupees}"

    def __str__(self):
        return f"Money: ₹{self._indian_format(self.rupees)}"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self.rupees = other.rupees

    def __hash__(self):
        return hash(self.rupees)

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.rupees < other.rupees

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(other.rupees + self.rupees)

    def __radd__(self, other):
        if other == 0:
            return self

        if not isinstance(other, Money):
            return NotImplemented

        return Money(other.rupees + self.rupees)



    @staticmethod
    def _indian_format(number):
        sign = "-" if number < 0 else ""
        number = abs(number)

        s = str(number)

        if len(s) <= 3:
            return sign + s

        last_three = s[-3:]
        remaining = s[:-3]

        parts = []

        while remaining:
            parts.append(remaining[-2:])
            remaining = remaining[:-2]

        parts.reverse()

        return sign + ",".join(parts) + "," + last_three



fee1 = Money(149000)
fee2 = Money(25000)

print("Fee 1:", fee1)
print("Fee 2:", fee2)
print("Fee 1 + Fee 2:", fee1 + fee2)

programme_fees = [
    Money(149000),
    Money(125000),
    Money(175000)
]

total = sum(programme_fees)

print("Programme fees:", programme_fees)
print("Total:", total)


fees = [
    Money(149000),
    Money(50000),
    Money(250000),
    Money(75000)
]

sorted_fees = sorted(fees)

print("Sorted:", sorted_fees)

a = Money(50000)
b = Money(50000)

money_set = {a, b}

print("Equal objects:", a == b)
print("Set:", money_set)
print("Set size:", len(money_set))

try:
    print(Money(1000) + 12.5)
except TypeError as e:
    print("TypeError:", e)