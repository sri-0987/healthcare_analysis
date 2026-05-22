from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_details(self):
        pass
    
class Patient(Person):
    def __init__(self, patient_id, name, age, gender, city):
        self.__patient_id = patient_id  # encapsulation
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city

    def get_details(self):
        return f"Patient: {self.name}"


class Doctor(Person):
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def get_details(self):
        return f"Doctor: {self.name}"