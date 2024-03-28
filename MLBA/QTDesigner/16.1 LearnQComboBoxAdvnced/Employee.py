import json

class Employee:
    def __init__(self,fullName,gender,city):
        self.fullName=fullName
        self.gender=gender
        self.city=city
    def __str__(self):
        return json.dumps(self.__dict__)