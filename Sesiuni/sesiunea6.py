# '''Sa intelegem ce sunt, care sunt particularitatile si cum se folosesc ciclurile repetitive:
# while
# while else (optional)
# for
# for else (optional)
# Sa putem controla iteratiile cu:
# break
# continue'''
#
# # While / while else
#
# i = 0
# while i <= 3: # for face incrementarea automat spre deosebire de while
#     print(i)
#     i += 1
# else:
#     print('am terminat ciclul')
#
# # For / for else
# '''Se executa un bloc de cod pentru fiecare valoare din range
# Range seamana cu slicing. Ne spune:
# De unde incepem? Default e 0
# Pana unde iteram?
# Optional: pasul
# Optional: la final se poate pune else
# aceasta zona se executa o data, la final'''
#
# for i in range(4):
#     print(i)
# else:
#     print('am terminat')
#
# # For
# '''Se parcurge o colectie si se salveaza fiecare element intr-o variabila
# La fiecare iteratie, variabila se va suprascrie cu valoarea actuala
# Rand pe rand, se vor parcurge toate elementele dintr-o colectie
# '''
# culori = ['rosu', 'albastru', 'verde', 'galben', 'mov']
# for culoare in culori:
#     print(f'Culoarea mea preferata e {culoare}')
#
# # Break
# '''Cuvantul cheie ‘break’ va opri iteratia
# Practic se iese automat din loop
# Nu se mai executa codul de după break, din cadrul unui for/while
# '''
# for i in range(999):
#     if i == 3:
#         break
#     print(i)
#
# # Continue
# '''Cuvantul cheie ‘continue’ va sari peste iteratia actuala
# E un fel de skip
# Se va sari peste blocul de cod de după skip, care tine de for/while
# '''
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)


# Cicluri repetitive
#
# Exerciții - studiu în workshopul de weekend

# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ‘Mașina mea preferată este x’.
# Fă același lucru cu un for each.
# Fă același lucru cu un while.

# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# favourite_car = 'Mercedes'
# for car in cars:
#     if car == favourite_car:
#         print(f'Masina preferata este {car}')
#     print(car)

# i = 0 # indexul fiecarui element din lista cars
# while i < len(cars):
#     if cars[i] == favourite_car:
#         # print(f'masina preferama este {cars[i]}')
#         # break
#         i += 1
#         continue
#         # print(f'masina preferama este {cars[i]}')
#     print(i, cars[i])
#     i += 1 # sau i = i + 1
#
# print(cars[0])




# 2. Aceeași listă:
# Folosește un for else
# În for
# Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
# În else:
#   Printează lista.

# nu va modifica nimic in lista
# why: car sufera modificari, dar nu vor fi rescrise in lista
# for car in cars:
'''cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
favourite_car = 'Mercedes'
    if car == cars[0] or car == cars[-1]:
        print(car)
        continue
    car = car.upper()
    print(car)'''

'''cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
favourite_car = 'Mercedes'
i = 0
for i, car in enumerate(cars):
    # car = car.upper()
    if cars[0] == car or cars[-1] == car:
        continue
    cars[i] = car.upper()
    print(i, car)
else:
    print(cars)'''

'''Bogdan s
for i, car in enumerate(cars):
    if cars[i] == cars[0] or cars[i] == cars[-1]:
        continue
    cars[i] = car.upper()

print(cars)
asa e bine ?'''

'''# Corneliu Mihai Gherman
for i in range(len(cars)):
     if 0 < i < len(cars) - 1: # nu capitalizeaza si primul si ultimul element al listei
        cars[i] = cars[i].upper()

else:
    print(cars)'''

#
# 3. Aceeași listă:  # putem gasi cu ce am facut mai suus
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Iterează prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
#    Printează ‘am găsit mașina dorită de dvs’
#    Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
#    Printează ‘Am găsit mașina X. Mai căutam‘

cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
car_for_sale = 'Mercedes'
i = 0

'''for car in cars:
    if car_for_sale == car:
        print(f'Am găsit mașina Dv: {car_for_sale}')
        break
    else:
        print('Mai cautam')'''

# 4. Aceeași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
#
# Dacă mașina e Trabant sau Lăstun:
#    Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# Printează S-ar putea să vă placă mașina x.

'''cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
car_for_sale = 'Mercedes'
i = 0

for car in cars:
    if car in ('Lăstun', 'Trabant'): # Lastun si Trabant aici e un tuple
        cars.remove(car)
        continue
    print(f'S-ar putea să vă placă mașina: {car}')
print(cars)'''

'''Sesiunea 7'''
# 5. Modernizează parcul de mașini:
#
# Crează o listă goală, masini_vechi.
# Iterează prin mașini.
# Când găsesti Lăstun sau Trabant:
# Salvează aceste mașini în masini_vechi.
# Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# Printează Modele vechi: x.
# Modele noi: x.

'''masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
wanted = ['Lăstun', 'Trabant']
masini_vechi = []

for index, masina in enumerate(masini):
    # if masina == 'Lăstun' or masina == 'Trabant':
    if masina in wanted:
        masini_vechi.append(masini[index])
        masini[index] = 'Tesla'
print(masini)
print(masini_vechi)'''


# 6. Având dict:
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# Vine un client cu un buget de 15000 euro.
#
# Prezintă doar mașinile care se încadrează în acest buget.
# Iterează prin dict.items() și accesează mașina și prețul.
# Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
# Iterează prin listă.

'''pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

for key, value in pret_masini.items():
    if value <= 15000:
        print(f'Puteti alege masina {key}')
'''

# 7. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterează prin ea.
# Afișează de câte ori apare 3 (nu ai voie să folosești count).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
counter = 0
for nr in numere:
    if nr == 3:
        counter += 1
print(counter)


# 8. Aceeași listă:
# Iterează prin ea
# Calculează și afișează suma numerelor (nu ai voie să folosești sum).
suma = 0
for nr in numere:
    suma += nr
print(suma)



# 9. Aceeași listă:
# Iterează prin ea.
# Afișază cel mai mare număr (nu ai voie să folosești max).
max = -10000
for nr in numere:
    if nr > max:
        max = nr
print(max)

min = 10000
for nr in numere:
    if nr < min:
        min = nr
print(min)

# 10. Aceeași listă:
# Iterează prin ea.
# Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# Afișază noua listă.


for index, nr in enumerate(numere):
    if nr > 0:
        numere[index] = nr * -1
print(numere)


# 11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișează cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for nr in alte_numere:
    if nr % 2 == 0:
       numere_pare.append(nr)
    else:
       numere_impare.append(nr)
    if nr > 0:
       numere_pozitive.append(nr)
    else:
       numere_negative.append(nr)
print(f'pare {numere_pare}')
print(f'impare {numere_impare}')
print(f'pozitive {numere_pozitive}')
print(f'negative {numere_negative}')


# 12. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# https://www.youtube.com/watch?v=lyZQPjUT5B4

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
lista_goala = []
# pasii 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(len(alte_numere)):
    for j in range (i+1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            aux = alte_numere[i]
            alte_numere[i] = alte_numere[j]
            alte_numere[j] = aux
print(alte_numere)

# print(f'lista sortata: {sorted(alte_numere)}') # cea mai eficienta varianta

'''sa mai incercam si alti sorting algorithms de pe google

pas 1: 
compar elementul cu indexul 0 cu tot ce urmeaza dupa el pana la finalul listei.
pasul 2:
Compar elementul cu indexul 1 cu tot ce urmeaza dupa el pana la finalul listei.
pas 3: compar elementul cu indexul 2 cu tot ce urmeaza dupa el pana la finalul listei.
.
.
.
pana la len(lista)
'''
'''
asa se face in c++
a = 1
b = 2
aux = 0

aux = a
a = b
b = aux'''

# a, b = b, a # asa se face in python



#
# Exerciții Recomandate - studiu individual                                        .
#
# 1. Revizualizează sesiunile din această săptămână și ia notițe în caz că ți-a scăpat ceva.
#
# 2. Vizualizează din cursul  ‘Primii pași în Programare’ de la sectiunile de mai jos:
# Structuri de date
# Flow Control
