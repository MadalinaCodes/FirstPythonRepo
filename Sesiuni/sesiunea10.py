'''sa ne concentram in pauza pe Git si pe GitHUub
pe 17 nu o sa fie Daniel, reprogramam pentru vineri 20'''

'''lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3= list

print(type(lista1), type(lista2), type(lista3))

class Car:
    # fields - atribute
    make = 'Dacia'
    model = None
    year = 2022
    color = None
    viteza = 0
    def accelerate(self):
        self.viteza = self.viteza + 10
        print(self.viteza)
        print('Vruum Vruum!', self.viteza)

    def print_self(self):
        print(self.make, self.year, self.viteza)

    def stop(self):
        print('Stop!')
        self.viteza = 0

# dictionar = {
#         'make': 'Dacia'
#         'model': None}

car1 = Car()
car2 = Car()
print(car1.make, car1.year, car1.viteza)
print(car2.make, car2.year)
car1. print_self()
car1.accelerate()
car2.accelerate()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.stop()



class Client:
    user = 'Madalina'
    parola = 'asdada'

    def ascunde_parola(self):
        self.parola = len(self.parola) * '*'

    def afiseaza_parola(self):
        print(self.user, self.parola)

print(Client.user)
print(Client.parola)
lista1 = list
client1 = Client()
client1.ascunde_parola()
client1.afiseaza_parola()
lista1 = [1, 2, 3, 4]
print()
'''

from datetime import date
class Om:
    nume = None
    varsta = None
    greutate = None
    data_nastere = None

    def __init__(self, nume, varsta, greutate, data_nastere):
        print('sunt in constructor')
        self.nume = nume
        self.varsta = varsta
        self.greutate = greutate
        self.data_nastere = data_nastere
        print(f'am atribuit {nume} {varsta} {greutate} {data_nastere} lui self\n') # \n e varianta lui enter in programare si adauga un rand nou
    def print_self(self):
        print('sunt in functia print self\n')
        print(self.nume, self.data_nastere, self.greutate, self.varsta)

    def __str__(self):
        return f'{self.nume}, {self.data_nastere}'

# om1 = Om('Madalina', 0, 3, date.today())
# om2 = Om('Bogdan', 0, 3, date.today())
# om1.print_self()
# print('\n')
# om2.print_self()





# Implementati urmatoarele clase, folosind notiuni OOP

# 1.Clasa Cerc
#     Atribute: rază, culoare
#     Constructor pentru ambele atribute
#     Metode:
# descrie_cerc() - va PRINTA culoarea și raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

'''class Cerc
    raza = raza
def __init__(self, raza, culoare):
self.raza = raza
self.culoare = culoare


def descriere_cerc(culoare, raza):
    print(culoare, raza)

def aria(raza):
    self.aria =
'''








# 2. Clasa Dreptunghi
#      Atribute: lungime, lățime, culoare
#      Constructor pentru toate atributele
#      Metode:
# descrie()
# aria()
# perimetrul()
# schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().

