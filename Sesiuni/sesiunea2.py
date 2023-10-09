''''
Partea 1 - Setup, Variabile, Tipuri de date

Exerciții - studiu în workshopul de weekend


7. Citește de la tastatură:
lungimea;
lățimea.
   Afișează: 'Aria dreptunghiului este x'.


lungime = float(input('lungime: ')) # secvential mai intai se citeste input apoi se face typecasting in float
latime = float(input('latime: '))
arie = lungime*latime
print(f'Aria este {arie} centimetri')

'''

''' 

8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
afișează de câte ori apare cuvântul 'the';
9. Același string:
Afișează de câte ori apare cuvântul 'the';
Printează rezultatul.

'''


# string = 'Coral is either the stupidest animal or the smartest rock'
# look_for = 'the '
# print(string.count(look_for))

'''

str = 'Coral is either the stupidest animal or the smartest rock'
count = 0
for i in range(0, len(str) - 2):
    if str[i] == 't' and str[i+1] == 'h' and str[i+2] == 'e' and str[i+3] == ' ':
        count+=1

print(count)

'''




# 10. Același string:
# Folosește un assert ca să verifici dacă acest string conține doar numere.


# print("Initial String: ", string)
#
# # Using isdigit()
# if string.isdigit():
# 	print("String contains all numbers")
# else:
# 	print("String doesn't contains all numbers")






# 11. Exercițiu:
# citește de la tastatură un string de dimensiune impară;
# afișează caracterul din mijloc.


# string = input('Introduceti string de dimensiune impara')
# lungime_string = len(string)
# if len(string) % 2 == 1:
#     index_mijloc = round(lungime_string / 2) - 1
#     print(lungime_string/2-1)
#     print(round(lungime_string/2 - 1))
#     print(string[index_mijloc])
# else:
#     print('Stringul are dimensiune para')

# pentru aflarea mijlocului
# string = input('Stringul de dimensiune impara')
# lungime_string = len(string)
# if lungime_string % 2 == 1:
#     index_mijloc = round(lungime_string / 2) - 1
#     print(string[index_mijloc])
# else:
#     print('Stringul are dimensiune para')


'''Corneliu Mihai Gherman09:35
str = 'Coral is either the stupidest animal or the smartest rock'
count = 0
for i in range(0, len(str)):
    if str[i] == 't' and str[i+1] == 'h' and str[i+2] == 'e':
        count+=1

print(count)

# Corneliu Mihai Gherman10:08
text = input('Introduceti textul: ')
caracter_cautat = text[round(len(text) / 2)]
if len(text) % 2 == 0:
    print('Textul introdus are un numar de caractere par!')
else:
    print(f'Caracterul cautat este: {caracter_cautat}')
'''






# 12. Folosind o singură linie de cod :
# citește un string de la tastatură (ex: 'alabala portocala');
# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.


# string = input(':')
# a, b = string.split(' ')
# ## c, d = a, b
# ## print(c, d)
#
# print(a, b)















# 13. Exercițiu:
# citește un string de la tastatură (ex: alabala portocala);
# salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

'''eu - incercat - nu merge sa scot ultimul caracter si mai trebuie sa capitalizez
st = input('text: ')
st = input('text: ')
# aflam dimensiunea
dimensiune = len(st)
print('dimensiunea ', dimensiune)
# scoate si ne returneaza primul si ultimul element
first = [st[0]]
last = st.pop()
print('primul element: ', first)
print('ultimul element: ', last)
print('lista', st)
'''




# 14.Exercițiu:
# citește un user de la tastatură;
# citește o parolă;
# afișează: 'Parola pt user x este ***** și are x caractere';
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
#
# eg: parola abc => ***
#       parola abcd => ****
'''
#facut in sesiunea 3 bine
user = input('user ')
parola = input('parola ')
parola_afisata = len(parola) * '*' # cornel - sa ii dea dumnezeu sanatate
print(f'Parola pt user {user} este {parola_afisata} și are {len(parola)} caractere')
print(f'Parola pt user {user} este {len(parola) * "*"} și are {len(parola)} caractere') # sau asa

#l = ('1') incepuse asta pana sa fie in
'''




#
#  Partea 2 - Operatori, condiționale
#
# Exerciții - studiu în workshopul de weekend
#
# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.
#
# 8.
# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''eu - done
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
if x == y == z and x > 0 and y > 0 and z > 0:
    print('trunghi echilateral')
elif x == y != z or x == z != y or x != y == z:
    print('trunghi isoscel')
else:
    print('triunghi oarecare')
'''

# 9. Citește o literă de la tastatură.
#     Verifică și afișează dacă este vocală sau nu.
'''eu - done
vocale = 'aeiouAEIOU'
litera = input('litera: ')

if any(char in vocale for char in litera):
    print(f'{litera} e vocala')
else:
    print(f'{litera} e consoana')
'''

''''# rezolvat mai bine de daniel
vocale = 'aeiouAEIOU'
litera = input('litera: ')
if litera in vocale:
    print(f'{litera} e vocala')
else:
    print(f'{litera} e consoana')
'''




#
# 10.Transformă și printează notele din sistem românesc în  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
''' eu - done
nota = float(input('nota '))
# problema propusa de bianca-ana beu nota = nota * - 1
# if nota < 0:
#     nota = nota * -1
# print(nota)
if nota >= 9:
    nota = 'A'
    print('A')
elif nota >= 8:
    nota = 'B'
    print('B')
elif nota >= 7:
    nota = 'C'
    print('C')
elif nota >= 6:
    nota = 'D'
    print('D')
elif nota >= 4:
    nota = 'E'
    print('E')
else:
    nota = 'F';
    print('F')
'''

# 11.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
''' eu - done
x = int(input('x = '))
nrcifre = len(str(x))
if nrcifre >= 4:
    print(f'{x} are minim 4 cifre')
else:
    print(f'{x} are mai putin de 4 cifre')
'''

# 12.Verifică dacă x are exact 6 cifre.

''' eu - done
x = int(input('x = '))
nrcifre = len(str(x))
if nrcifre == 6:
    print(f'{x} are exact 6 cifre')
elif nrcifre > 6:
    print(f'{x} are mai mult de 6 cifre')
else:
    print(f'{x} are mai putin de 6 cifre')
'''

# 13.Verifică dacă x este număr par sau impar (x e int).

''' eu - done
x = int(input('x = '))
if x % 2 == 0:
    print(f'{x} e par')
else:
    print(f'{x} e impar')
'''


# 14.      x, y, z (int)
# Afișează care este cel mai mare dintre ele?
# discutie in sesiunea 3 - iese doar cu un for, ce a pus corneliu e bine
'''
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

print(x, y, z)
min = 1000
# 100 35 1 4 6 9 6 89 90 86 11

if x >= y and x >= z:
    print(f'{x} e cel mai mare')
elif y >= x and y >= z:
    print(f'{y} e cel mai mare')
elif z >= x and z >= y:
    print(f'{z} e cel mai mare')
else: print('Toate numerele egale')
'''

'''Corneliu Mihai Gherman
max_number = 0
numbers = [21, 23, 121, 32, 43]

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)'''

# 15.
# X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
'''# facut cu echipa - bine
x = float(input('x = '))
y = float(input('y = '))
z = float(input('z = '))
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print('triunghi valid')
else:
    print('triunghi invalid')
'''

''' eu - done dar cu laturi
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
if x + y > z and x + z > y and y + z > x:
    print('triunghi valid')
else:
    print('triunghi invalid')
'''

# 16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# Citește de la tastatură un int x
# Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''inceput doar
string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('x = '))

'''









# 17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
#
# 18. Același string.
# Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
# Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
# output: 'Coral is either the stupidest animal or the smartest'
#
#
# 19. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
#
# 20.  Citește de la tastatură un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat

'''incercare
# sttas = input('introdu string: ')
# count = 0
# for i in range(0, len(sttas)):
'''

# 21. Având stringul '0123456789'
# Afișează doar numerele pare
# Afișează doar numerele impare
# (hint: folosește slicing, controlează din pas)
''' eu
st = '0123456789'
count = 0
for i in range(0, len(st)):
    if i % 2 == 0:
        print(f'numar par {i}')
    else:
        print('')

for i in range(0, len(st)):
    if i % 2 == 1:
        print(f'numar impar {i}')
    else:
        print('')
'''




# Exerciții Recomandate - studiu individual                                        .
#
# 1. Revizualizează sesiunile din această săptămână și ia notițe în caz că ți-a scăpat ceva.
#
# 2. Vizualizează din cursul  ‘Primii pași în Programare’ de la sectiunile de mai jos:
# Variabile și Tipuri;
# Operatori și Flow Control.
