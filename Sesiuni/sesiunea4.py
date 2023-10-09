list1 = ["abc", 34, True, 40, "male", "male"]
print(list1)
print(list1[0]) #primul element
print(len(list1))

#liste simplu inlantuite, dublu inlantuite
lista = [1, 2, "asd", True, 5, 8]
print(lista[-1]) # ultimul element
print(lista[3:5]) # afiseaza mai multe elemente => [True, 5] incepe la indexul 3 si se opreste inainte de indexul 5

lista.append(None)
lista.append(None)
print(lista)

nn=None
print(type(nn))

print(lista[0:3:6]) #slicing

print(lista[0:-1])

print(lista[::2]) # numara din 2 in doi de la o, adica index 0, 2, 4 etc

print(lista[::-1]) #afiseaza lista de la sfarsit spre inceput
print(lista[::])

thisdict = {
    "brand": "Volvo",
    "model": "XC60",
    "year": 2011

}

print(thisdict)
print(thisdict['brand'])
print(len(thisdict))

mydict = {
    "2": 34,
    "4": "porasdats" #cheile trebuie sa fie unice si nu se pot modifica, doar valorile se pot modifica
}

print(mydict["4"])
mydict["a"] = "wertyui"
print(mydict.values())

mydict = {6: 34, 3: "porasdats", "a": "wertyui"}

ll = mydict.values()
print(list(ll))

mydict = {"masisni": ["", "", ""]}

# in dictionar pui un user de exemplu

mydict = {"masini": {
    "brand": [1, 2, 3]
}}

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    {"1": 2, "3": 4},
    "234234"
]
print(matrice[2]['3'])

print(mydict['masini']['brand'][2]) #asta e practic o matrice



## seturi // nu sunt indexate seturile
culori = {'alb', 'rosu', 'galben'}
print(culori)
print(len(culori))

ss = {1, 2, 3, 3, 3} #setul are acolade si lista are paranteze patrate
ff = {3, 4, 5}
print(ss, ff) #afiseaza doar valori unice
print(ss.intersection(ff))
# cc = [1, 2, 2] # asta e lista
# print(cc) # afiseaza toate valorile listei, nu doar pe cele unice ca la set

print(set(ss).union(set(ff)))

# Tuple
thistuple = ("apple", "banana", "cherry") # un tuplu e constant/imutabil, nu putem adauga alte elemente
print(thistuple)
print(len(thistuple))

ss
print(ss)
lista = [1, 2, 3, 3, 3]
print(set(lista))# transforma lista in set
print(list(ff)) # transforma setul in lista




# spoiler pentru tema
count = 0
for element in ss:
    print(element)

    if element == 2:
        print("L-am gasit pe 3")
        count = count + 1 # count ++

print(f"L-am gasit pe 3 de {count} ori")
