#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod
from factory.absfact import Appam, Puttu,Paneer, Paratta
class Order(metaclass=ABCMeta):
    @abstractmethod
    def get_order(type_of_meals):
        pass
class SouthIndianDish(Order):
    def get_order(type_of_meals):
        if type_of_meals == "Appam":
            return Appam()
        if type_of_meals == "Puttu":
            return Puttu()
        if type_of_meals == "curry":
            return Appam()
class NorthIndianDish(Order):
    def get_order(type_of_meals):
        if type_of_meals == "Paneer":
            return Paneer()
        if type_of_meals == "Paratta":
            return Paratta()
        if type_of_meals == "curry":
            return curry()
        if type_of_meals == "Tea":
            return drink()
class FinalOrder:
    def get_menu(self,type_of_meals):
        if type_of_meals == "SouthIndian":
            return SouthIndianDish
        if type_of_meals == "NorthIndian":
            return NorthIndianDish
