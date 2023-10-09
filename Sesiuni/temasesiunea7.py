# Cicluri repetitive
#
#
# 13. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
#    User alege un număr
#    Programul îi spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitări! Ai ghicit!

import random
numar_secret = random.randint(1,30)
numar_ghicit = None

while numar_secret != numar_ghicit:
    numar_ghicit = int(input('numar: '))
    if numar_ghicit > numar_secret:
        print('Numarul introdus este prea mare.')
    elif numar_ghicit < numar_secret:
        print('Numarul introdus este prea mic.')
    else:
        print('Ai ghicit numarul')










# 14. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333
#
#
# 15.
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)
#
# Exerciții Recomandate - studiu individual                                        .
#
# 1. Revizualizează sesiunile din această săptămână și ia notițe în caz că ți-a scăpat ceva.
#
# 2. Vizualizează din cursul  ‘Primii pași în Programare’ de la sectiunile de mai jos:
# Structuri de date
# Flow Control
#
