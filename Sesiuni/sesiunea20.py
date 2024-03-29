"""https://www.geeksforgeeks.org/python-design-patterns/"""

# Design Patterns - stabilirea arhitecturii proiectului: ce date intre, ce date ies (vine un user, se logheaza, cumpara ceva si a plecat)
# logica acestui flow are nevoie de design patterns ce ii vor fi de folos pentru o mai usoara dezvoltare
# aceste design patterns este o lectura in oop, ne ajuta la design in backend


"""Facem o clasa Singleton atunci cand avem nevoie de o singura instanta pe tot parcursul proiectului, 
cum ar fi o baza de date sau o clasa utilitara ce lucreaza cu fisiere
-------------instanta/obiect ce se instantiaza o singura data-------------------"""


class SingletonClass:
    __instanta = None
    # putem sa punem cate atribute vrem noi
    bec = False
    kilometraj = 0
    # destination_path = ""
    # source _path = ""


    def __init__(self, bec=False): # acest construc
        self.sector = bec

    def __new__(cls, *args, **kwargs):
        # se apeleaza ca si constructorul atunci cand creem o instanta in clasa noastra,
        # cls acceseaza atribute si metode din clasa in sine, in timp ce self acceseaza din instante
        if cls.__instanta is None: #
            # acest obiect se instantiaza o singura data in a lifetime
            cls.__instanta = object.__new__(cls) # object.__new__ este obiectul de baza in python cum e integer spre exemplu

            # de vreme ce instanta noastra a fost reluata la inceput, urmatoarele instante vor fi identice cu aceasta
            return cls.__instanta

    def move_logs(self):
        pass
    def move(self):
        self.kilometraj +=100

    def aprinde_bec(self):
        self.bec = True

    def stinge_bec(self):
        self.bec = False

    '''exemnplu pentru bec'''
    # def __str__(self):
    #     string = "aprins" if self.bec else "stins" # inline if
    #     return f"becul este {string}"

    def __str__(self):
        return f"km {self.kilometraj}"


instance1 = SingletonClass()
instance1.move()
instance1.move()

instance2 = SingletonClass()
instance2.move()
instance2.move()

instance3 = SingletonClass()
instance3.move()

# is verifica egalitatea a 2 obiecte in totalitate (valorile dar si adresa de memorie)
if instance1 is instance2 and instance2 is instance3:
    print("toate instantele sunt la fel")



"""tema"""

class PresedinteRomania:
    _instance = None  # Variabila pentru a stoca instanta unica

    def __new__(cls):
        # Verificăm dacă instanța există deja
        if not cls._instance:
            # Dacă nu există, creăm instanța și o stocăm în variabila de clasă
            cls._instance = super(PresedinteRomania, cls).__new__(cls)
        return cls._instance

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'
# Testăm Singleton
a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')


"""Vasile Mocanu08:41
brb
Meet IT Factory08:41
https://www.geeksforgeeks.org/python-design-patterns/
Corneliu Mihai Gherman09:26
eu vreau chiar mai multe becuri :)
Dorian Ciuca09:26
nu vreau nici un bec
Alexandru Danicel09:27
A singleton pattern can be implemented in three different ways. They are as follows:

Module-level Singleton
Classic Singleton
Borg Singleton

Exista si Picard Singelton????
Dorian Ciuca09:35
adica 0 = 0 dar 0 = 0.1 nu este acelasi lucru
0 + 0 = 0 0 + 0.1 = 0 dar nu este exact 0
Vasile Mocanu10:01
Se instanteaza instanta intantelor instantei cu instantele instantelor instantei( furata de la un coleg/a)"""