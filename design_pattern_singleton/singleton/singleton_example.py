#!/usr/bin/env python3

'''You should use the singleton pattern
   when your app needs a globally accessible,
   lazy loaded object that has only one instance.'''

class Singleton(type):
    _instance = {}
    def __init__(cls, name, bases,attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Myclass(metaclass=Singleton):
    def __init__(self):
        print ("class")

    # @classmethod
    # def get_instance(cls):
    #     return Myclass()
    pass

if __name__ == '__main__':
    A = Myclass()
    print(A).__str__()
    B= Myclass()
    assert A is  B
