class Person:
    species = "homosapien"

    def __init__(self, species = "homosapien", age=21, name_first="McLovin", name_last="Jones"):
        self.species = species
        self.age = age
        self.name_first = name_first
        self.name_last = name_last

class Student(Person):

    def __init__(self, species = "homosapien", age=21, name_first="McLovin", name_last="Jones", student_id):
        Person.__init__(species, age, name_first, name_last)
        self.student_id = student_id

class Teacher(Person)
