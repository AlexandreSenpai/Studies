'''In python we can easily create an class using type
'''

Dog = type('Dog', (), {})
class Cat: pass

print(Dog) # <class '__main__.Dog'>
print(type(Dog)) # <class 'type'>
print(type(Dog) == type(Cat)) # True

'''Using metaclasses we can change class attrs before initializing it
'''

class Meta(type):
    def __new__(self, class_name: str, bases: tuple, attrs: dict) -> type:
        
        new_attrs = {}
        
        for key in attrs:
            if key.startswith('__'):
                new_attrs[key] = attrs[key]
            else:
                new_attrs[key.upper()] = attrs[key]

        return type(class_name, bases, new_attrs)

class Test:
    UEPA = 1

class Fox(metaclass=Meta):
    first_propr: int = 1
    second_propr: int = 2

    def __init__(self) -> None:
        self.instance_only: str = "instance only propr."

'''Using metaclasses to apply singleton pattern.
'''

class SingletonMeta(type):

    _instances = {}

    def __call__(self):
        if len(self._instances) == 0:
            self._instances[self] = super().__call__()
        
        return self._instances[self]

class Singleton(metaclass=SingletonMeta):

    CONNECTED: bool = True

    def say_hi(self) -> str:
        return "Hi xD"

if __name__ == '__main__':
    fox = Fox()
    print(fox.FIRST_PROPR) # 1
    print(fox.SECOND_PROPR) # 2
    print(fox.instance_only) # this was not changed cause the __init__ is a function and we cannot access declared variables on it.

    s1 = Singleton()
    s2 = Singleton()
    
    print(id(s1) == id(s2)) # True
    print(s1.CONNECTED) # True
    print(s2.CONNECTED) # True

    s2.CONNECTED = False

    print(s1.CONNECTED) # False
    print(s2.CONNECTED) # False

    '''Even if we only change the s2 instance propr this change will affect all the instances since it's a singleton class builded using metaclass'''

    