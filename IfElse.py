# if
piesa_faina = True
print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca numarul este par printam acest lucru
# altfel printam impar
nr = 4
# ce inseamna par? se imparte exact la 2
# ce inseamna ca se imparte la 2? ne da restul 0
if nr % 2 == 0:
    print('numarul este par')
else :
    print('numarul este impar')

# este un nr pozitiv?
if (nr > 0):
    print('pozitiv')
else:
    print('nr nu este pozitiv')


    # tema - putem sa transpunem in IfElse si problema cu bunicul si bunica
mama = False
tata = False
bunicul = True
bunica = False
if mama == True or tata == True or (bunicul == True and bunica == True):
    print(mama or tata or (bunicul and bunica))
else:
    print('copil orfan')

    # tema - daca operatorul are sub 18 ani, nu poate paria
operator = 27
if operator > 18:
    print('major - poate paria')
else:
    print('minor - nu poate paria')
#if, else if, else
# cum ne saluta robotelul in functie de ora?
# luam date de la tastatura
# ne asiguram ca sunt transformate din string in integer

# ora = int(input('Introdu ora'))
# if ora < 0:
#     print('ora invalida, ora negativa')
# elif ora <= 11:
#     print('buna dimineata')
# elif ora <= 18:
#     print('buna ziua')
# elif ora <= 21:
#     print('buna seara')
# elif ora <= 24:
#     print('noapte buna')
# else:
#     print('ora invalida, mai mare decat 24')
# Am pus blockul de cod de mai sus comentariu selectandu-l pe tot si apasand CTRL + /

# robotel telefonic
optiunea = int(input('alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiunea == 1:
    print('ati ales ro')
elif optiunea == 2:
    print('ati ales eng')
else:
    print('nu am identificat optiunea, mai incearca')
