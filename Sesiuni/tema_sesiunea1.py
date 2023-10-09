# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# variabila - o zona din memorie care tine o anumita valoare, se scriu cu litera mica, nu putem pune spatiu, este urmata de obicei de operatorul de atribuire =
# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
# string
var_str = 'Madalina'
# int
var_int = 27
# float
var_float = 27.50
# bool
bool = False

# Observație: Valorile vor fi alese de tine după preferințe.

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(type(var_str))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
var_float = round(var_float)
print(var_float)

# Verifică tipul acesteia.
print(type(var_float))

# 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
print(f'Numele meu este {var_str}')
print('Varsta mea este: ' + str(var_int))
print(f'Varsta mea este: {var_int}')
print(f'Am atatia bani in buzunar: {var_float}')
print('E adevarat ca am atatia bani in buzunar? ' + str(bool)) #varianta 1
print(f'E adevarat ca am atatia bani in buzunar? {bool}') # varianta 2

# Rezolvă nepotrivirile de tip prin ce modalitate dorești. # done

# 6. Citește de la tastatură:
# numele;
# prenumele.
#     Afișează: 'Numele complet are x caractere'.

nume = input('Nume: ')
prenume = input('Prenume: ')
length = len(nume+prenume)
print('Numele complet are ' + str(len(nume+prenume)) + ' caractere')
print(f'Numele complet are {length} caractere')