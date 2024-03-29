# mostenire
# abstractizare
# incapsulare
# polimorfism

# "Cu cat copacul este mai stufos cu atat este mai frumos" by Daniel Paun
# -> cu cat proiectul este mai stufos CONCEPTUALIZAT in 1. 2. 3. 4.
# cu atat este mai frumos (lizibil, usor de inteles, usor de digerat de fiecare dev)
from abc import ABC, abstractmethod
class MInterface(ABC):
    @abstractmethod
    def descrie(self):
        raise NotImplementedError

    @abstractmethod
    def vopseste(self, culoare):
        raise NotImplementedError

    @abstractmethod
    def accelereaza(self, viteza):
        raise NotImplementedError

class Masina(MInterface):
    __culoare = 'gri' # atribut privat -> modificam cu setter
    viteza_actuala = 0 # atribut privat -> modificam cu setter
    __culori_disponibile = ['gri', 'albastru', 'rosu']
    marca = None # atribut public
    model = None # atribut public
    __viteza_maxima = None # __ privat

    def __init__(self, model, viteza_maxima):
        self.__viteza_maxima = viteza_maxima
        self.__model = model

    def vopseste(self, culoare):
        if culoare in self.__culori_disponibile:
            self.__culoare = culoare
        else:
            raise Exception('culoarea introdusa nu exista')

    def descrie(self):
        # TODO: NEED TO IMPLEMENT this method
        pass

    def accelereaza(self, viteza):
        if viteza >= 0 and viteza <= self.__viteza_maxima:
            self.__viteza_actuala = viteza
        else:
            raise NameError

    def get_viteza_actuala(self):
        return self.__viteza_actuala

    def get_culoare(self):
        return self.__culoare

m = Masina(model='Volvo', viteza_maxima=220)
t = Masina(model='Toyota', viteza_maxima=300)
m.accelereaza(10)
print(m.get_viteza_actuala())
m.accelereaza(30)
print(m.get_viteza_actuala())
# m.vopseste('asd')
m.vopseste('albastru')
print(m.get_culoare())

