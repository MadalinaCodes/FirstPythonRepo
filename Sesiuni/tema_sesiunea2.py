'''Operatori, condiționale

Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.

1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
'''
# if inseamna daca
# else inseamna altfel
# if verifica daca o conditie este indeplinita si da o anumita comanda, iar else da alta comanda daca conditia nu este indeplinita.

'''

2. Verifică și afișează dacă x este număr natural sau nu.
'''

#x = int(input("Enter a number:"))
#
# if x >= 0:
#     print(f" {x} is a natural number")
# elif x < 0:
#     print(f" {x} is not a natural number")
# else:
#     print(f" {x} is not a number")


'''discutii ipotetice la curs
x = input('enter a number')
if type(x) == int: # asta nu merge ca e string orice input daca nu punem int inainte
    print('nr naural')
elif type (x)

sau

if isinstance() care e la fel ca if type(x)
'''
'''
    Corneliu
    Mihai
    Gherman
    # codul asta da int orice ar fi
    
    def input_validate(input_text: str):
        string = input(input_text)
        while string.__contains__('.') or string.__contains__(',') or string.isalpha():
            print('Date incorecte! Incearca din nou!')
            string = input(input_text)
        return string
'''


'''if x is number
x = input('x= ')'''




'''

3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
'''
# if x > 0:
#     print('numar pozitiv')
# elif x < 0:
#     print('numar pozitiv')
# else:
#     print('numar neutru')



'''


4. Verifică și afișează dacă x este între -2 și 13.

'''
# if x >= -2 and x <= 13:
#     print(f'{x} este cuprins intre -2 si 13')
# else:
#     print(f'{x} nu este cuprins intre -2 si 13')

'''

5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

'''
# y = int(input('introdu un numar: '))
# if x - y < 5 or y - x < 5:
#     print('diferenta dintre cele 2 numere este mai mica decat 5')
# else:
#     print('diferenta dintre cele 2 numere nu este mai mare decat 5')

'''

6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.

'''
# if not(x >= 5 and x <= 27):
#     print(f'numarul {x} nu este intre 5 si 27')
# else:
#     print(f'{x} este intre 5 si 27')

'''

7.
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
'''
x = int(input('x = '))
y = int(input('y = '))

if x == y:
    print(f'x = {x}, y = {y}')
elif x > y:
    print(f'{x} e mai mare decat {y}')
else:
    print(f'{y} e mai mare decat {x}')

