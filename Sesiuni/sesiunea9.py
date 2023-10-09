

def return_the_sixth(list):
    if len(list) < 6:
        raise IndexError('Lista nu are 6 elemente cel putin.')
    else:
        return list[6]


    # try:
    #     return list[6]
    # except IndexError as e:
    #     # write error in logs here
    #     print(e)
    #     return list[-1]

the_sixth = return_the_sixth([30, 20, 10])
print(the_sixth)

def divide(x, y):
    try:
        result = x // y
        return result
    except ZeroDivisionError as e:
        print('Impartirea la 0 nu este permisa.')
        return -1

    else:
        print('divide done')
        return result
    finally:
        print('acest cod se executa oricum')

nr1= int(input('nr1: '))
nr2= int(input('nr2: '))
print(divide(nr1, nr2))

'''Corneliu Mihai Gherman08:49 # aici ia in considerare orice tip de eroare
def numar(numar):
    try:
        return int(numar)

    except Exception as e:
        e = 'Adauga un numar!'
        return e


print(numar('asda'))
si aici un exemplu'''

'''Alexandru Danicel09:08
functiile trebuie create (adica declarate)
dupa care trebuie folosite adica apelate
Alexandru Danicel09:09
declararea este partea cu "def" apelarea este cand scri doar numele functiei test(x,y)

Alexandru Danicel09:09
test este numele, x si y sunt doua variabile pe care le dau functiei'''