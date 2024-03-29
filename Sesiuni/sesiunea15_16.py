import random
import time

'''
class Om:
    nume = 'asd'
    prenume = 'werwer'
    data_nastere: str
    adresa:str
    has_job = True
    has_car = True

class ListaOameni:

    def __init__(self, l_oameni):
        self.lista_oameni = l_oameni

    def __iter__(self):
        return iter(self.lista_oameni)

    def __next__(self):
        return next(self.lista_oameni)

o1 = Om()
o2 = Om()
o3 = Om()

lo = [o1, o2, o3]
lista_oameni = ListaOameni(lo)

for om in lista_oameni:
    print(om.nume, om.prenume)
'''
# alta varianta
'''
o1 = Om()
o2 = Om()
o3 = Om()

nume = 'ashd'
prenume = 'ahdg'

nume1 = 'asda'
prenume1 = 'hfhd'

nume2 = 'yuo'
prenume2 = 'fgdhs'

lo = [(nume, prenume), (nume1, prenume1), (nume2, prenume2)]

for element in lo:
    print(element[0], element[1])
'''


'''
from datetime import datetime
from functools import wraps
def timp_executie(functia_originala):
    @wraps(functia_originala)
    def wrapper(*args, **kwargs):
        t1 = datetime.now()
        result = functia_originala(*args, **kwargs)
        t2 = datetime.now()
        t = t2 - t1
        print(result)
        print(f'{functia_originala.__name__} a fost executata in {t}')
        return result
    return wrapper

@timp_executie
def sum_of_list(lista):
    sum = 0
    for nr in lista:
        sum = sum + nr
    return sum

@timp_executie
def abc():
    return 'abc'

@timp_executie
def a1234():
    return '1234'

nr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_of_list(nr_list)

# t1 = datetime.now()
# print(sum_of_list(nr_list))
# t2 = datetime.now()
# t = t2-t1
# print(t)


'''
# exercitii sesiuna16
#4. Implementați următorii decoratori:
# timeit – decorator care măsoară timpul de execuție al unei funcții
# logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții
#
'''
def logger(functia_originala):
    @wraps(functia_originala)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        result = functia_originala(*args, **kwargs)
        print(result)
        return result
    return wrapper

class ReverseIterator:
    def __init__(self, note):
        self.iterator = iter(note[::-1])

    def __iter__(self):
        return self.iterator

    def __next__(self):
        return next(self.iterator)

note = [1, 2, 3, 4, 5]

rev_it = ReverseIterator(note)
print(next(rev_it))
print(next(rev_it))
print(next(rev_it))
print(next(rev_it))
'''


def get_random_numbers():
    total_numere = 0
    while True:
        if total_numere == 6:
            return
        nr = random.randint(1, 49)
        yield nr
        time.sleep(1)
        total_numere += 1
        print(total_numere)

note = [1, 2, 3, 4, 5]
gen_nr = get_random_numbers()
# print(next(gen_nr))
gen_nr1 = get_random_numbers()
# for nr in gen_nr:
#     print(nr)

for nr1, nr2 in zip(gen_nr, gen_nr1):
    print(nr1, nr2)

# Alexandru Danicel11:37
def gen():
    total_nr = 0
    while True:
        if total_nr >= 6:
            nr = "All 6 nr are out"
        else:
            nr = random.randint(6, 49)
        yield nr
        total_nr += 1


gen_nr = gen()
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
vha-mrmx-mxz




















