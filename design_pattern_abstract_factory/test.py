#!/usr/bin/env python3
from factory.mainfactory import SouthIndianDish, NorthIndianDish,FinalOrder
print("The menu .........[S.I].: Appam / Puttu / \n                  [N.I].: Paneer / Paratta  \n")


FN =FinalOrder()
#*******************************************************************************
Southindian = FN.get_menu("SouthIndian")
Appam = Southindian.get_order("Appam")
Appam.cook()
Appam.curry()
#_______________________________________________________________________________
Southindian = FN.get_menu("SouthIndian")
Puttu = Southindian.get_order("Puttu")
Puttu.cook()
Puttu.curry()
#_______________________________________________________________________________
northindian = FN.get_menu("NorthIndian")
paneer = northindian.get_order("Paneer")
paneer.cook()
paneer.curry()
#_______________________________________________________________________________
northindian = FN.get_menu("NorthIndian")
paratta = northindian.get_order("Paratta")
paratta.cook()
paratta.curry()
paratta.drink()
