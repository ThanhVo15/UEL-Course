class Employee:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return str(self.id) + "|" + str(self.name) + "|" + str(self.age) + "|" + str(self.gender)


