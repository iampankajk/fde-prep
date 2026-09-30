import logging
from carworks import delivery

log = logging.getLogger(__name__)

def expensive(fleet, above=1000000):
    return [car for car in fleet if car.price > above]

def pending(fleet):
    return [car for car in fleet if not car.is_delivered]

def by_fuel(fleet):
    counts = {}
    for car in fleet:
        counts[car.fuel_type] = counts.get(car.fuel_type, 0) + 1
    return counts

def cost_sheet(fleet):
    return {car.car_id: delivery.delivery_cost(car.destination) for car in fleet}

def stats(fleet):
    if not fleet:
        log.warning("stats() called on an empty fleet")
        return {"cars": 0, "total_value": 0, "average_price": 0,
                "delivered": 0, "pending": 0}
    total = 0
    for car in fleet:
        total += car.price
    return {
        "cars": len(fleet),
        "total_value": total,
        "average_price": round(total / len(fleet)),
        "delivered": len(fleet) - len(pending(fleet)),
        "pending": len(pending(fleet)),
    }