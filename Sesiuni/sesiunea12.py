from abc import ABC

class Animal(ABC): # ABC ne permite sa cream clase abstracte
    '''CLASA DE TIP INTERFATA, TIPAR PENTRU VIITOARELE CLASE CE MOSTENESC'''
    @abstractmethod # decorator ce defineste metoda de mai jos
    def sound(self):
        raise NotImplementedError # e la fel ca pass, dar mai bun

    @abstractmethod
    def sleep(self):
        raise NotImplementedError

    def __get_all(self):
        pass

class Dog(Animal):
    __name = 'Gigel'
    def sound(self):
        pass

    def sleep(self):
        raise NotImplementedError

    def get_name(self):
        raise self.__name

    def set_name(self, name):
        # functie pt a ma asigura ca name respecta anumite reguli
        if self.__check_name(name) == True
        self.__name = name
    # raise NameNotRespectConditionsERROR

    def __check_name(self, name):
        if name == '':
            return False
        if len(name) <= 5:
            return False
        return True

d = Dog()
d.name = "Asdasd"










# Cerinte miniproiect  A
#
# Mașină
# Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori disponibile (set), înmatriculată (bool)
#    Culoare = gri - toate mașinile când ies din fabrică sunt gri
#    Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
#    Culori disponibile = alege tu 5-7 culori
#    Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
#    Înmatriculată = False
# Constructor: model, viteza_maxima
# Metode:
# descrie() - se vor printa toate atributele, în afară de culori_disponibile
# înmatriculare() - va schimba atributul înmatriculată în True
# vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare, dacă viteza e mai mare decât viteza_max - masina va accelera până la viteza maximă
# franeaza() - mașina se va opri și va avea viteza 0










'''
OOP

1. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)


 2. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total
Telefon |      7       |       700       | 49000

Indiciu pentru dată: https://www.geeksforgeeks.org/get-current-date-using-python/


'''