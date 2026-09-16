learners = {
    "Aarav": ["P", "P", "A", "P", "A"],
    "Diya": ["P", "P", "P", "P", "P"],
    "Kabir": [],
    "Meera": ["P", "A", "A", "P"]
}


def percent(marks):
    if not marks:
        return 0.0

    present = marks.count("P")
    return present / len(marks) * 100


for name, marks in learners.items():
    attendance = percent(marks)

    if attendance < 80:
        print(f"{name} {attendance:.1f}% BELOW 80")