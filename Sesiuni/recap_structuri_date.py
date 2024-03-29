
lista = [1, '2', 3.5, True, False, 3.5, {1:'2'}, []]
lista.append("  ")
lista.pop()
lista.pop()
lista.remove(3.5)
print(lista.index(3.5))
print(lista)

set = {1, 2, 3, 3, 2, 1}
print(type(set))
print(set)
set.add(44)
print(set)



prop = 'Ana are mere'
print(prop[3:9])