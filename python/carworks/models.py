class Car:
    VALID_FUELS = ("Petrol", "Diesel", "Hybrid", "EV")
    PIPELINE = ("Manufactured", "In Transit", "Delivered")

    def __init__(self, car_id, model, fuel_type, price, destination):
        if fuel_type not in self.VALID_FUELS:
            raise ValueError(f"{fuel_type!r} is not one of {self.VALID_FUELS}")
        if price <=0:
            raise ValueError("a price must be positive")
        self.car_id = car_id
        self.model = model
        self.fuel_type = fuel_type
        self.price = price
        self.destination = destination
        self.__status = self.PIPELINE[0]
        self.__history = [self.PIPELINE[0]]

    @property
    def status(self):
        return self.__status

    @property
    def is_delivered(self):
        return self.__status == "Delivered"

    def history(self):
        return list(self.__history)

    def advance(self, to):
        if to not in self.PIPELINE:
            raise ValueError(f"{to!r} is not a pipeline status")
        if self.PIPELINE.index(to) <= self.PIPELINE.index(self.__status):
            return False
        self.__status = to
        self.__history.append(to)
        return True

    def __repr__(self):
        return f"Car({self.car_id!r}, {self.model!r}, {self.price})"

    def __str__(self):
        return (f"{self.car_id}  {self.model:<8}{self.fuel_type:<8}"
                f"Rs {self.price:>9,}  {self.destination:<10}{self.status:<13}")


