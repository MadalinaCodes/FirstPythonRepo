
''' am pus in comentariu pana la exerciutiul 9
CARS = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] # cand vezi o variabila cu litere mari stii ca ea e folosita in mai multe functii

# def print_cars(cars):
#     print('lista masini: ', CARS)

def print_cars(cars = ['a', 'b']):
    print(cars)

def suma2nr(a, b):
    # print(a+b)
    suma = a + b
    return suma



def print_cars_reversed():
    print('lista masini: ', CARS[::-1])

lista = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

print_cars(cars = lista)

# print_cars()
# print_cars_reversed()

print('out of main')

if __name__ == '__main__':
    print('main')

gigel = suma2nr(1, 3)
print(gigel)
# suma2nr(6,2)

# exercitii
# Funcții
#
# Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa. Dacă funcția are return, printează răspunsul.

# 1.
# Funcție care să calculeze și să returneze suma a două numere
def sum_2_nr(nr1, nr2):
    suma = nr1 + nr2
    return suma

# 2.
# Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar.
def is_par(nr):
    if nr % 2 == 0:
        return True
    else:
        return False
# 3.
# Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)
def total_chars(
        nume,
        prenume,
        nume_mijlociu):
    total = len(nume) + len(prenume) + len(nume_mijlociu)
    return total
# chem functia
# t = total_chars(
#     nume = 'andon',
#     prenume = 'madalina',
#     nume_mijlociu = 'atat')
# print(t)

a = int(input('introdu nr1: '))
b = int(input('introdu nr2: '))
print(sum_2_nr(a, b))
print(sum_2_nr(5, 37))
print(sum_2_nr(123123, 345345))
print(sum_2_nr(2345345, 346345))

print(is_par(23))
print(is_par(24))
print(is_par(25))

t = total_chars(
    nume = 'andon',
    prenume = 'madalina',
    nume_mijlociu = 'atat')
print(t)


# 4.
# Funcție care returnează aria dreptunghiului

def aria_dreptunghiului(lungime, latime):
    aria = lungime * latime
    return aria

print(aria_dreptunghiului(50, 100))
print(aria_dreptunghiului(2, 4))

# 5.
# Funcție care returnează aria cercului

def circle_area(R):
    pi = 3.14
    aria = pi * R * R

print(circle_area(50))
print(circle_area(160))

# 6.
#Funcție care returnează True dacă un caracter x se găsește într - un string dat și False dacă nu găsește.

def find(str1, str2):
    if str1 in str2:
        return True
    else:
        return False

# 7.
# Funcție fără return, primește un string și printează pe ecran:
# Numărul de caractere lower case este x
# Numărul de caractere upper case este y

def numar_mare_mic(x):
    numar_mare = 0
    numar_mic = 0
    for char in x:
        if str(char).islower():
            numar_mic = numar_mic + 1
        elif str(char).isupper():
            numar_mare = numar_mare + 1
        else:
            continue
    print(f'Am gasit {numar_mare} litere scrise cu majuscule')
    print(f'Am gasit {numar_mic} litere scrise cu minuscule')
numar_mare_mic("AJHDKaajshA")

'''
'''
# Cornel - Sa-i dea Dumnezeu sanatate
def num_upp_low(string):
    up_count = 0
    low_count = 0
    for char in string:
        if str(char).isalpha():
            if str(char).isupper():
                up_count += 1

            else:
                low_count += 1

    print(f'Lower characters found: {low_count}')
    print(f'Upper characters found: {up_count}')
'''
'''
# 8. # sesiunea 9 cu echipa
# Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.

def pozitiv_only(lista):
    nr_pozitive = []
    for nr in lista:
        if nr > 0:
            nr_pozitive.append(nr)
    return nr_pozitive
listapozitive = pozitiv_only([1, 3, 5, -6, -3, 8])
print(listapozitive)



# 9.
# Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
# Primul număr x este mai mare decat al doilea număr y
# Al doilea număr y este mai mare decat primul număr x
# Numerele sunt egale.

def compare(x, y):
    if x > y:
        print(f'{x} e mai mare decat {y}')
    elif y > x:
        print(f'{y} e mai mare decat {x}')
    else:
        print('Numerele sunt egale')

compare(5, 5)
'''

# 10.
# Funcție care primește un număr și un set de numere.
# Printează ‘am adaugat numărul nou în set’ + returnează True
# Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False

'''def add_number(number, set_numere: set):
    if number not in set_numere:
        set(set_numere).add(number)
        print('am adaugat numărul nou în set')
        return True
    else:
        print('nu am adaugat numărul în set. Acesta există deja')
        return False
set1 = {4, 5, 7}
print(add_number(8, {3, 5, 8}))
print(set1 = add_number(8, {3, 5, 8})'''

'''def add_number(number, set_numere: set):
        if number not in set_numere:
            set_numere.add(number)
            print("Am adaugat numarul in set")
            return True
        else:
            print("Nu am adaugat. Exista deja")
            return False

set1 = {4, 5, 7}
print(add_number(8, {3, 5, 8}))'''

'''
# varianta cu exceptie
def add_number(number, set_numere: set):
    try:
        if number not in set_numere:
            set_numere.add(number)
            print("Am adaugat numarul in set")
            return True
        else:
            print("Nu am adaugat. Exista deja")
            return False
    except Exception:
        print(Exception('Error'))

try:
    print(add_number(8, 3, 5, 8))
except TypeError:
    print('Error')
'''
''''''
# Bogdan s11:00
def add_number(number, set_numere):
    try:
        if number not in set_numere:
            set_numere.add(number)
            print("Am adaugat numarul in set")
            return True
        else:
            print("Nu am adaugat. Exista deja")
            return False
    except Exception:
        print(Exception("Error"))

try:
    print(add_number(8, 3, 5, 8))
except TypeError:
    print("Error")
# Alexandru Danicel11:03
def add_number(number, set_numere):
   try:
        if number not in set_numere:
            set_numere.add(number)
            print("Am adaugat numarul in set")
            return True
        else:
            print("Nu am adaugat. Exista deja")
            return False
   except AttributeError as e:
        print(e)


# set1 = {4, 5, 7}
print(add_number(1, (3, 5, 8)))

# 11.
# Funcție care primește o lună din an și returnează câte zile are acea lună.
#
# 12.
# Funcție calculator care să returneze 4 valori.Suma, diferența, înmulțirea, împărțirea a două numere.

# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
#
# 13.
# Funcție care primește o listă de cifre(adică doar (0 - 9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# = > dict
# {
#     0: 0
#     1: 2
#     2: 0
#     3: 1
#     4: 0
#     5: 3
#     6: 0
#     7: 2
#     8: 0
#     9: 1
# }
#
# 14.
# Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
#
# 15.
# Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
# Exemplu: dacă dăm numărul 3, suma va fi 6(0 + 1 + 2 + 3)
#
# 16.
# Funcție care primește 2 liste de numere(numerele pot fi dublate). Returnați numerele comune.
#
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}
#
# 17.
# Funcție care să aplice o reducere de preț.
# Dacă produsul costă 100 lei și aplicăm reducere de 10 %. Pretul va fi 90 de lei.
# Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110 % e invalidă.
#
# 18.
# Funcție care să afișeze data și ora curentă din România.
# (bonus: afișază și data și ora curentă din China)

# 19.
# Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta:)






