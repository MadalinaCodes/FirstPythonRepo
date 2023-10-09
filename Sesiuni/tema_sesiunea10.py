# Implementati urmatoarele clase, folosind notiuni OOP

# 1.Clasa Cerc
#     Atribute: rază, culoare
#     Constructor pentru ambele atribute
#     Metode:
# descrie_cerc() - va PRINTA culoarea și raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
'''facut in sesiunea 11'''
import math


raza = float(input("Enter the radius of the circle::\n"))
culoare = input('Culoare preferata?')


class Circle:
    raza = None
    culoare = None

    def __init__(self,raza,culoare):
        self.raza = raza
        self.culoare = culoare

    def print_self(self):
        print(self.raza, self.culoare)

    def diametru(self):
        d = 2 * self.raza
        return d

    def circumferinta(self):
        c = 2 * math.pi * self.raza
        return c

    def aria(self):
        a = math.pi * (self.raza * self.raza)
        return a


my_circle = Circle(raza=raza,culoare=culoare)
my_circle.print_self()

print(my_circle.circumferinta())
print(my_circle.diametru())
print(my_circle.aria())




'''incercare

class Cerc
    raza = raza
def __init__(self, raza, culoare):
self.raza = raza
self.culoare = culoare
Pi = 3.14


def descriere_cerc(culoare, raza):
    print(culoare, raza)

def aria(raza):
    self.aria =

def



'''





# 2. Clasa Dreptunghi
#      Atribute: lungime, lățime, culoare
#      Constructor pentru toate atributele
#      Metode:
# descrie()
# aria()
# perimetrul()
# schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().


class Dreptunghi:
    # atribute
    lungime = None
    latime = None
    culoare = None

    #constructor
    def __init__(self, lungime, latime, culoare):
        # self ne ajuta sa assignam valori atributelor obiectului curent
        # (obiectelor viitoare)
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    # metodele clasei
    def descrie(self):
        """printeaza toate atributele din obiectul curent(self)"""
        print(f"Lungime: {self.lungime} "
              f"Latime {self.latime} "
              f"Culoare {self.culoare}")

    def aria(self):
        aria = self.lungime * self.latime
        return aria

    def perimetru(self):
        perimetru = 2 * self.lungime + 2 * self.latime
        return perimetru

    def schimba_culoarea(self, noua_culoare):
        """
        Această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă
        culoare și va suprascrie atributul self.culoare.
        Poți verifica schimbarea culorii prin apelarea metodei descrie().
        """
        self.culoare = noua_culoare

# aceste variabile le folosim pentru a creea un dreptunghi
lungime = float(input("Give me Lungime: "))
latime = float(input("Give me Latime: "))
culoare = input("Give me culoare: ")

# suntem in viitor. in clasa dreptunghi variabilele lungime, latime si culoare
# vor ajunge in self.lungime, self.latime respectiv self.culoare
#acestea prin intermediul "self" apartin variabilei "my_dreptunghi"
my_dreptunghi = Dreptunghi(
    lungime=lungime,
    latime=latime,
    culoare=culoare
)
my_dreptunghi.descrie()

# functia print afiseaza rezultatul functiei aria() apelata prin intermediul
# my_dreptunghi
print("aria este: ", my_dreptunghi.aria())

# functia print afiseaza rezultatul functiei perimetru() apelata prin intermediul
# my_dreptunghi
print("perimetrul este: ", my_dreptunghi.perimetru())


# apelam functia
my_dreptunghi.schimba_culoarea(
    noua_culoare=input("Spune-mi noua culoare a dreptunghiului de mai sus: ")
)

my_dreptunghi.descrie()
