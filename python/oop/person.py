class Person:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student(Person):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Professor(Person):
    def __init__(self, name, subject):
        super().__init__(name) 
        self.subject = subject