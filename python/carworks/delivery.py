import logging

log = logging.getLogger(__name__)

#: Road distance in km from the Noida plant.
DISTANCE_KM = {
    "Noida": 5, "Delhi": 25, "Jaipur": 270, "Kanpur": 470,
    "Lucknow": 480, "Mumbai": 1400, "Bengaluru": 2150
}

#: (upper km bound, rupees per km). The first slab the distance fits into wins.
SLABS = ((50, 40), (300, 22), (1000, 16), (999999, 12))

BASE_FEE = 2500

def distance_to(city):
    if city not in DISTANCE_KM:
        raise KeyError(f"no distance on file for {city!r}")
    return DISTANCE_KM[city]

def rate_for(km):
    for upper, rate in SLABS:
        if km <= upper:
            return rate
    raise ValueError(f"no slab covers {km} km")

def delivery_cost(city):
    km = distance_to(city)
    cost = BASE_FEE + km * rate_for(km)
    log.debug("cost to %s: %d km at Rs %d/km = Rs %d", city, km, rate_for(km), cost)
    return cost

def eta_days(city):
    km = distance_to(city)
    return max(1, round(km/350) + 2)

def priority(car):
    if car.price >= 1500000:
        return "HIGH"
    if car.fuel_type in ("EV", "Hybrid"):
        return "HIGH"
    if car.price >= 800000:
        return "MEDIUM"
    return "LOW"