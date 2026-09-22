import random

class Hat:
    houses = ["Delhi", "Gurugram", "Pune", "Bangalore"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        return f"{name} is in {house}"

print(Hat.sort("Pankaj"))