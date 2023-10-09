def printGreeting():
    print("Buna ziua! Bine ati venit!")

def printGreetingByName(nume, prenume):
    print(f'Buna ziua, {nume} {prenume}!')

def mediaNr(a, b, c):
    return (a + b + c) / 3

def piValue ():
    return 3.14 # return e ultima instructiune care se intampla intr-o functie, automat se si inchide programul dupa aceea // tot ce vrem sa se execute trebuie pus deasupra la return

#  exercitiu
# daca persoana e majora, altfel false
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False


# zona de apelare (desktop)
printGreeting()
printGreeting()
printGreetingByName('Andon', 'Madalina')
printGreetingByName('Andon', 'Sonia')
printGreetingByName('Andon', 'Catalin')
print(mediaNr(3,3,4))
print(piValue())
print(verificareMajor(18))

# se ia varsta utilizatorului
age = int(input('introduceti varsta dvs'))
if verificareMajor(age): # if verifica daca e True
    print('Cont creat. Bine ai venit in aplicatie!')
else:
    print('Nu ai varsta minima necesara pentru a paria(18)')

# in oop vorbim de variabile si functii, variabilele se vor numi proprietati sau fields si functiile se vor numi metode