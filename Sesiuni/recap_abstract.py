from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        raise NotImplementedError
    
    def sleep(self):
        raise NotImplementedError

class Dog(Animal):
    def sound(self):
        print("hamham")

class Cat(Animal):
    def stop(self):
        print("meow")

dog = Dog()
dog.sound()