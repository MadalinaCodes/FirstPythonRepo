'''discutie legata de tema de la sesiunea 2

x = int ('enter number: ')
x = int(x)

# % - modulo
# este restul impartirii

if x % 3 == 0:
    print(f'rest: {x%2}')
    print(f'numarul {x} este divizibil cu 3')
else:
    print(f'rest: {x % 2}')
    print(f'numarul {x} este impar')

Dorian Ciuca08:38
text = input('Introduceti textul: ')
caracter_cautat = text[round(len(text) / 2)]
if len(text) % 2 == 0:
    print('Textul introdus are un numar de caractere par!')
else:
    print(f'Caracterul cautat este: {caracter_cautat}')
'''

# 1. introduceti un string de la tastatura. verificati daca acesta contine numere.
'''se rezolva ca cel de dinainte cu aeiou

vocale = 'aeiouAEIOU'
litera = input('litera: ')
if litera in vocale:
    print(f'{litera} e vocala')
else:
    print(f'{litera} e consoana')'''

string = input('text: ')
numere = '1234567890'
if string in numere:
    print(f'{string} contine numere')
else:
    print(f'{string} e un string')