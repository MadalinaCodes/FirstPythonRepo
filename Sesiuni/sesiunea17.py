'''my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_iterator = iter(my_list)

print(next(my_iterator)) # [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(next(my_iterator)) #[3, 4, 5, 6, 7, 8, 9, 10]
print(next(my_iterator)) # [4, 5, 6, 7, 8, 9, 10]
print(next(my_iterator)) # [5, 6, 7, 8, 9, 10]
print(next(my_iterator)) # [6, 7, 8, 9, 10]
print(next(my_iterator)) # [7, 8, 9, 10]
print(next(my_iterator)) # [8, 9, 10]
print(next(my_iterator)) # [9, 10]
print(next(my_iterator)) # [10]
print(next(my_iterator)), list(my_iterator) # [] -> Exception StopIteration
'''

'''
import time

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
another_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
my_iterator = iter(my_list)
another_iterator = iter(another_list)

# ideea iteratorilor este de a fi consumati o singura data (parcursi)
# ideea listelor este de a fi parcurse de cate ori avem nevoie

for e1, e2, in zip(my_list, another_list):
    print(e1, e2)
print(list(my_iterator), list(another_iterator))

my_iterator = iter(my_list)
another_iterator = iter(my_list)
while True:
    try:
        print(next(my_iterator), next(another_iterator))
        time.sleep(1)
    except StopIteration:
        print("Am terminat de iterat")
        break'''

# def div(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print('Impartirea la 0 nu este posibila')
#         return None
#
# print(div(10, 0))


'''# exercitiul 3
alfabet = 'abcdefghijklmnopqrstuvwxyz'
iterator_alfabet = enumerate(alfabet) # [(0, a), (1, b), ...]

# for pozitie, litera in enumerate(alfabet):
#     print(f'eu sunt {litera} la pozitia {pozitie}')
# print(list(iterator_alfabet))

while True:
    element = next(iterator_alfabet) # (0, a) ... urmatorul element etc
    pozitie = element[0]
    litera = element[1]
    print(f'eu sunt {litera} la pozitia {pozitie}')
print(list(iterator_alfabet))'''


"""Decorators extra
Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nasterii 
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat, folosind un decorator `@require_login` 
– o metoda logout, fara params, care delogheaza userul.


Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.
"""

'''
from functools import wraps

class User:
    def __init__(self, nume, prenume, email, parola, data_nasterii):
        self.nume = nume
        self.email = email
        self.__parola = parola # atribute private cu ajutorul "__" in fata variabilei
        self.data_nasterii = data_nasterii
        self.__este_logat = False

    def require_login(functia_originala):
        # acest wrapper are functia de a acoperi o alta functie dandu-i proprietati in plus
        def wrapper(self, *args, **kwargs):
            print(self.__este_logat)
            if self.__este_logat == True:
                result = functia_originala(self, *args, **kwargs)
                return result
            else:
                print('userul nu este logat')

        return wrapper

    def login(self, email, parola):
        # util pentru documentarea codului
        """
        :param self:
        :param email:
        :param parola:
        :return:
        """
        if email == self.email and parola == self.__parola:
            self.__este_logat = True

    def logout(self):
        """
        - o metoda de logout, fara params, care delogheaza userul
        :return:
        """
        self.__este_logat = False

    @require_login # decoratorul se ruleaza inaintea functiei
    def get_info(self):
        """
        - o metoda get_info, care va returna toate informatiile despre user DOAR DACA este logat.
        *** folosind un decorator @require_login ***

        :return:
        """
        if self.__este_logat == True:
            print(self.nume, self.email, self.__parola, self.data_nasterii)
        else:
            print("userul nu este logat")

    @require_login
    def change_pass(self, new_pass):
        self.__parola = new_pass


# valorile date ca parametru clasei se vor duce in self-ul fiecarei instante (user1, user2, .._
user1 = User('asd', 'asddd', 'asd@email.com', '1234', '2 ianuarie 1991')
user2 = User('ert', 'jhdgjd', 'ert@email.com', '4567', '2 ianuarie 1991')
user1.login("asd@email.com",'1234')
user1.get_info()
user1.logout()
user1.get_info()

user1.login('asd@email.com', '1234')
user1.change_pass('123')
user1.logout()
user1.login("asd@email.com",'123')
user1.get_info()
'''

"""Corneliu Mihai Gherman10:14
my_string = 'ABCDEFGHIJKLMN
my_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def alphabet(ls: list):
    my_iterator = iter(ls)
    for i in range(1, len(ls)):
        try:
            print(f'My name is {next(my_iterator)} and I am the number {i} in alphabet!')

        except StopIteration:
            print('End of line!')

alphabet(my_string)"""



'''exercitiu 3
Context Managers
Se da un fisier text hello.txt, care contine un text scurt. Deschideți fișierul și citiți conținutul, folosind urmatoarele 2 metode:
try - finally 
Fișierul se deschide înainte de try, folosind functia open
În interiorul try citim conținutul folosind functia read
În finally se închide fișierul
with (context manager)
Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fișierul, pentru ca context managerul face asta pentru noi.
'''
'''Alexandru
Danicel11: 46

file = [1, 2, 3, 4, ads]

try:
    file = open("requirements.txt", "r")
    print(file.read())
except:
    print("Error managing file")
finally:
    file.close()

with open("requirements.txt", "r") as file:
    print(file.read())'''

'''Decorators
Implementați următorii decoratori:
timeit – decorator care măsoară timpul de execuție al unei funcții 
logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții

'''

import time
from functools import wraps


def logger(functia_originala):
    @wraps(functia_originala)
    def wrapper(*args, **kwargs):
        result = functia_originala(*args, **kwargs)
        return result, args, kwargs
    return wrapper


def timeit(functia_originala):
    @wraps(functia_originala)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = functia_originala(*args, **kwargs)
        t2 = time.time() - t1
        print(t2)
        return result
    return wrapper

@logger
def calculate(a, b):
    return a + b


print(calculate(2, 4))


"""Corneliu Mihai Gherman12:00
def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if len(kwargs) != 0:
            return (f'Function\'s arguments: {args[0], kwargs}\n'
                    f'Function\'s result: {result}')
        else:
            return (f'Function\'s arguments: {args[0]}\n'
                    f'Function\'s result: {result}')"""