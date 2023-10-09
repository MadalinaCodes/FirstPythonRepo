ss = ['oaiealba', 'oaiealba', 'oaieneagra', 'oaiealba', 'oaieneagra'] # lista
ff = {3, 4, 5, 5, 5} # set

count_negre = 0
count_albe = 0
count_oi = 0
for element in ss:
    if element == 'oaieneagra':
        count_negre = count_negre + 1 # count ++
    elif element == 'oaiealba':
            count_albe = count_albe + 1
    if 'oaie' in element:
        count_oi += 1
print(count_negre, count_albe, count_oi)


cc = [3, 4, 5, 5, 5]
count = 0
for element in cc:
    if element == 5:
        count += 1
print(count)

lista = ['3', '4', '5', '33', 4, 3, 3]
string = '123456'
s = '3'

if s in string:
    '3' in '12345'
    # se ia primul string si se cauta in interiorul celui de-al doilea string
    print(f'l-am gasit pe {s} in {string}')

if s in lista:
    '3' in '3' '4' '5'
    # se cauta primul element (oricare tip de variabila ar fi) si se cauta in lista
    print(f'l-am gasit in lista')

