class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
        
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Delhi", "Pune", "Gurugram"]:
            raise ValueError("Invalid input")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

# We can add this function directly to class because it is related to Student class
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)
#     return student


if __name__ == "__main__":
    main() 
