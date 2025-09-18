'''
Animal.py

Module that includes classes Animal, Cat, Dog. For use with Animal_Journal.py

-------------------------------
OOP Notes
Pillars
- Inheritance
    - Child classes inherit methods and attributes from parent class
- Polymorphism
    - "Many forms"
    - Method Overloading
        - Changing behavior of a method given different arguments
    - Method Overriding
        - Changing behavior of a method inherited from a parent class
- Encapsulation
    - Having control over your attributes
        - Control with setter and getter methods
    - *** Can't make attributes private in python ***
    - Emulate by prefixing attributes with "_"
    - "__" = _{class_name}__{attribute_name}
- Abstraction
    - Handling complexity by hiding unnecessary information from the user
    - Achieved by using abstract classes (one or more abstract methods)
        - Abstract method => unimplemented method
    - abc (abstract base class)
'''
from abc import ABC, abstractmethod

class Animal(ABC):
    # Constructor
    def __init__(self, type, name, age, color):
        self._type = type
        self._name = name
        self._age = age
        self._color = color

    def getType(self):
        return self._type
    
    def setName(self, name):
        self._name = name

    def getOlder(self, years=1):
        self._age += years

    # Apstract method to be overridden by child classes
    @abstractmethod
    def makeNoise(self):
        pass

    def __str__(self):
        return f"Name: {self._name}, Type: {self._type}, Age: {self._age}, Color: {self._color}"

class Cat(Animal):
    def __init__(self, name, age, color):
        self._type = "cat"
        self._name = name
        self._age = age
        self._color = color

    def makeNoise(self):
        print("meow")

class Dog(Animal):
    def __init__(self, name, age, color):
        self._type = "dog"
        self._name = name
        self._age = age
        self._color = color

    def makeNoise(self):
        print("bark")

def main():
    '''
    Example for instantiating Animal objects.
    '''
    cat_1 = Cat("Garfield", 20, "orange")
    cat_1.makeNoise()
    cat_1.getOlder(15)
    print(cat_1)

    dog_1 = Dog("Fido", 12, "brown")
    print(dog_1)

    dog_1.setName("Buddy")
    print(dog_1)

# main block
if __name__ == "__main__":
    main()