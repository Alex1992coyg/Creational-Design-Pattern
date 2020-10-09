#!/usr/bin/env python3
''' prototype design pattern '''

from abc import ABCMeta, abstractstaticmethod
import copy

class InterfacePrototype(metaclass=ABCMeta):
    @abstractstaticmethod
    def clone():
        pass

class ConcreteClassRectangle(InterfacePrototype):
    def __init__(self, index=0, s="", l=[], d={}):
        self.i = index
        self.label = s
        self.Specification = l
        self.dimension = d

    def clone(self):
        return type(self)(
        self.i,
        self.label,
        self.Specification.copy(),
        self.dimension.copy())
    def __str__(self):
        return f"   index={self.i} \t s={self.label} \t ratio={self.Specification} \t d ={self.dimension}"

class ConcreteClassResize(InterfacePrototype):
    """concrete class 2"""

    def __init__(self, i=0, s="", l=[], d={}):
        self.index = i
        self.label = s
        self.Specification = l
        self.dimension = d
    '''deepcopy :copies and create new refrence for all level '''
    def clone(self):
        return type(self)(
            self.index,
            self.label,
            copy.deepcopy(self.Specification),
            copy.deepcopy(self.dimension))

    def __str__(self):
        return f"i={self.i} \t s={self.s} \t   ratio={self.l} \t d={self.d} "


if __name__ == "__main__":

    shape = ConcreteClassRectangle(
        1,
        "Rectangle",
        [1, 2, 3],
        {"length": 5, "width": 5, "height": 5}
    )
    print(f"shape {shape}")
    # print(type(shape ))

    reshape = shape.clone()
    reshape.label = "Resize"
    reshape.i = 2
    reshape.Specification[2] = 10
    print(f"shape {shape}")
    print(f"reshape {reshape}")
