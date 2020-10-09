#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod
class Menu(metaclass=ABCMeta):
    #two abstract method for main dish and curry
    @abstractmethod
    def cook(self):
        pass
    @abstractmethod
    def curry(self):
        pass
class Appam(Menu):
    name = " Appam "
    sidedish = " Egg "
    def cook(self):
        print( " South Indian breakfast  1.ready:  "+str(self.name) )
    def curry(self):
        print( "                           curry:  "+str(self.sidedish) )
class Puttu(Menu):
    name = " Puttu "
    sidedish = " kadala "
    def cook(self):
        print( " South Indian breakfast  2.ready:  "+str(self.name))
    def curry(self):
        print( "                          curry:   "+str(self.sidedish)  )
class Paneer(Menu):
    name = " Paneer butter masala "
    sidedish = " kuruma "
    def cook(self):
        print( " North Indian breakfast  1.ready:  "+self.name)
    def curry(self):
        print( "                           curry:  "+self.sidedish )
class Paratta(Menu):
    name = " Alu Paratta "
    sidedish = " chicken curry "
    hotdrink = " Tea"
    def cook(self):
        print( " North Indian breakfast  2.ready:  "+self.name)
    def curry(self):
        print( "                           curry:  "+self.sidedish )
    def drink(self):
        print( "                           Drink:  "+self.hotdrink)
