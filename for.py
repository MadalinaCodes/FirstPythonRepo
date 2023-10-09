# dalmatienii
# for i in range (1, 102):
#     print(f'Dalmatianul cu nr {i}')

# dalmatienii din 2 in 2
for i in range (1, 102, 2):
    print(f'Dalmatianul cu nr {i}')

numere = [3, 7, 10, 20, 30]
# parcurgere lista cu for prin intermediul indexului
for i in range (0, len(numere)):
    print(f'indexul curent este {i}')
    print(f'numarul curent este {numere[i]}')

# for each
s = 0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s = s + numar
print(f'Suma este {s}')

# tema - de cate ori apare 3 in [3, 2, 3, 5, 3, 3]

tema = [3, 2, 3, 5, 3, 3]
inc = 0 # increment https://sparkbyexamples.com/python/count-occurrences-of-element-in-python-list/
for i in tema:
    if (i == 3):
        inc = inc + 1
print(f'3 se repeta de {inc} ori')