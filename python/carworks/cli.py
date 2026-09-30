import logging

from carworks import delivery, report
from carworks.models import Car


log = logging.getLogger(__name__)

# MENU =  1  list the fleet
#   2  delivery cost sheet
#   3  statistics
#   4  advance the next pending car
#   0  quit

def seed_fleet():
    return [
        Car("C101", "Nexon", "Petrol", 850000, "Delhi"),
        Car("C102", "Creta", "Diesel", 1450000, "Lucknow"),
        Car("C103", "Swift", "Petrol", 750000, "Kanpur"),
        Car("C104", "City", "Hybrid", 1650000, "Delhi"),
    ]

def show_fleet(fleet):
    for car in fleet:
        print(f"{car}{delivery.priority(car):<8}eta {delivery.eta_days(car.destination)}d")


def advance_next(fleet):
    waiting = report.pending(fleet)
    if not waiting:
        log.info("nothing left to advance")
        print("Every car has been delivered.")
        return
    car = waiting[0]
    nxt = car.PIPELINE[car.PIPELINE.index(car.status) + 1]
    car.advance(nxt)
    log.info("%s advanced to %s", car.car_id, nxt)
    print(f"{car.car_id} is now {nxt}.")



def run(fleet, script=None):
    while True:
        if script is None:
            choice = input("choice: ")
        elif script:
            choice = script.pop(0)
        else:
            log.info("the script ran out")
            return
        log.info("menu choice %r", choice)
        if choice == "1":
            show_fleet(fleet)
        elif choice == "2":
            for car_id, cost in report.cost_sheet(fleet).items():
                print(f"  {car_id}  Rs {cost:,}")
        elif choice == "3":
            for key, value in report.stats(fleet).items():
                print(f"  {key:<14}{value:,}")
        elif choice == "4":
            advance_next(fleet)
        elif choice == "0":
            log.info("menu closed by the user")
            print("Bye.")
            return
        else:
            log.warning("unknown menu choice %r", choice)
            print("  Pick a number from the menu.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)-8s %(name)-18s %(message)s")
    run(seed_fleet())