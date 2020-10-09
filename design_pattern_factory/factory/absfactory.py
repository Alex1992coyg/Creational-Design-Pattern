#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod

class AgeLimit(metaclass=ABCMeta):

    @abstractmethod
    def calculate_eligibilty(self):
        pass

    # @abstractmethod
    # def qualification(self):
    #     pass

class Student(AgeLimit):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.qualifi = qualifi

    def calculate_eligibilty(self):
         if self.age < 25:
             return self.age
    # def qualification(self,degree):
    #     if self.quali == str(degree):
    #         return self.qualifi

    def __str__(self):
        return self.name + " [" +str(self.age)+"] "  +" so : eligible"

class NonStudent(AgeLimit):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.qualifi = qualifi
    def calculate_eligibilty(self):
        if self.age > 25:
            return self.age
    # def qualification(self,no_degree):
    #     if self.quali == str(no_degree):
    #         return self.qualifi

    def __str__(self):
        return self.name + " [" +str(self.age)+"] " +" not eligible"


class ExamCenter:
    def person_age(self,type_of_person):
        if type_of_person == "student":
            return Student("jo", 24)
        if type_of_person == "non_student":
            return NonStudent("dani",28)
