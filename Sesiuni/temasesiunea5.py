# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.
#
# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
#    Găsește 2 variante să le unești într-o singură listă.

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]

l3 = l1 + l2

l1.extend(l2)

print(l1)


# 4.
# Sortează și afișează lista generată la exercițiul anterior.
l1.sort()
print(l1)
# Sortează numărul 0 folosind o funcție.
# se face cu for
# Afișaza iar lista.




# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# Lista este goală.
# Lista nu este goală.
if len(l3) > 0:
    print('lista nu este goala')
else:
    print('lista este goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
l3.clear()
# del l3 # sterge toata lista
print(l3) # sterge continutul listei




# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
#
# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}

# print(dict1.keys())
# print(dict1.values())

for key in dict1:
    print(key, dict1[key])

# marim nota lui Dorel
dict1['Dorel'] = 6
print(dict1)

# dorel se muta din clasa

dict1.pop('Gigel')

#push baga un element in lista, pop scoate

# coleg nou
dict1['Ionica'] = 9
print(dict1)

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
#
# 10. Dorel a făcut contestație și a primit 6
# Modifică nota lui Dorel în 6
# Printează nota după modificare
#
#
# 11. Gigel se transferă din clasă
# Căuta o funcție care să îl șteargă
# Vine un coleg nou. Adaugă Ionică, cu nota 9
# Printează noii elevi
#
#
# 13.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# Adaugă în zilele_sapt ‘luni’
# Afișează zile_sapt

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

zile_sapt.add('luni')
print(zile_sapt)


# 14.Folosește un if și verifică dacă:
# Weekend este un subset al zilelor din săptămânii.
# Weekend nu este un subset al zilelor din săptămânii.

if weekend.issubset(zile_sapt):
    print('este subset')
else:
    print('nu este subset')

# 15. Afișează diferențele dintre aceste 2 seturi.

print(zile_sapt - weekend)
print('diferenta')
print(zile_sapt.difference(weekend))


# 16. Afișează intersecția elementelor din aceste 2 seturi.
#
#
# Exerciții Recomandate - studiu individual                                        .
#
# 1. Revizualizează sesiunile din această săptămână și ia notițe în caz că ți-a scăpat ceva.
#
# 2. Vizualizează din cursul  ‘Primii pași în Programare’ de la sectiunile de mai jos:
# Structuri de date
# Flow Control

'''exercitii facute cu echipa'''

# 12. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
#
# Declară o Listă cu 5 jucători
echipa = ['Hagi', 'Mutu', 'Ronaldo', 'Banel', 'Messi']
# Schimbari_efectuate = te joci tu cu valori diferite
schimbari_efectuate = 0
# Schimbari_max = 3
schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
jucator_schimbat = input('Jucatorul scos: ')
jucator_introdus = input('Jucatorul introdus: ')
# Efectuează schimbarea
# Șterge jucătorul scos din listă
# Adaugă jucătorul intrat
# Afișază a intrat x, a ieșit y, mai ai z schimbări

if schimbari_efectuate < schimbari_max and jucator_schimbat in echipa:
    schimbari_efectuate += 1
    echipa.remove(jucator_schimbat)
    echipa.append(jucator_introdus)
    print(f'A intrat {jucator_introdus}, a iesit {jucator_schimbat}, mai ai {schimbari_max - schimbari_efectuate} schimbari')
    print(echipa)
elif schimbari_efectuate == schimbari_max:
    print('Nu mai avem schimbari posibile')
else:
    print(f'Jucatorul {jucator_schimbat} nu se afla in echipa. Mai avem {schimbari_max - schimbari_efectuate} schimbari')



# Dacă jucătorul nu e în teren:
# Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
# Afișază ‘mai ai z schimbări’
#
# Testează codul cu diferite valori
#
# Google search hint
# “how to check if item is în list python”


'''
# program raul de alegere a celui care prezinta exercitiile

import random

da_team = ['Vasile', 'Valentin_Mihai', 'Corneliu', 'Raul', 'Anca', 'Bianca', 'Valentin_Sorin', 'Razvan', 'Ioana', 'Marius', 'Bogdan', 'Dorian', 'Madalina', 'Alexandru']
sesiune = 4 #deja au trecut 4 sesiuni
print(da_team)
while len(da_team) >= 1:
    prezinta_azi = random.choice(da_team)
    sesiune = sesiune + 1
    print(f'Sesiunea a {sesiune}-a, prezinta: {prezinta_azi}.')
    da_team.remove(prezinta_azi)
'''