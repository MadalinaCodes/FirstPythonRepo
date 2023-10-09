from datetime import date

# exemplu de variabila CONSTANTA (ce nu se schimba pe parcursul programului)
DATABASE_URL = "https://mydb.com"
USER = ""
PAROLA = ""

class Om:
    nume = None
    varsta = None
    greutate = None
    data_nastere = None


    def __init__(self, nume, varsta, greutate, data_nastere):
        self.nume = nume
        self.varsta = varsta
        self.greutate = greutate
        self.data_nastere = data_nastere

    def print_self(self):
        print("sunt in functia print self \n")
        print(self.nume, self.data_nastere, self.greutate, self.varsta)

    def __str__(self):
        return f"{self.nume}, {self.data_nastere}"



class Sofer:
    conduce_auto = None

    def __init__(self, conduce_auto):
        self. conduce_auto = conduce_auto


# intre cele doua paranteze din definirea clasei mentionam pe cine mostenim
# clasa Chef va mosteni atributele si metodele clasei Om
class Chef(Om, Sofer):

#'''mostenirea ne permite sa avem acces la atributele si functiile clasei parinte(superioare)'''

    def __init__(self, nume, greutate, varsta, data_nastere):
        super(Om, self).__init__(nume=nume, greutate=greutate, varsta=varsta, data_nastere=data_nastere)
        super(Chef, self).__init__()

    def make_salad(self):
        print('Am facut salata!')

    def make_fries(self):
        print('Am facut cartofii')

    def make_dishes(self):
        print('Am spalat vasele!')

class JapaneseChef(Chef):
    sushi_level = 10
    def make_sushi(self):
        print('sushi')

    def __init__(self, nume, varsta, greutate, data_nastere, sushi_level):
        # apelam obligatoriu constructorul din clasa parinte (superioara)
        super(Om, self).__init__(nume, greutate, varsta, data_nastere)
        super(Sofer, self).__init__(conduce)
        self.sushi_level = sushi_level

class ItalianChef(Chef):
    def make_pizza(self):
        print('pizza')


bucatar = Chef(nume='dan', varsta='24', greutate='75', data_nastere='03.03.03')
bucatar.print_self()

japan_chef = JapaneseChef('andrei', 23, 234, '03.03.03', 100, conduce=True)
japan_chef.print_self()

'''Getter: A method that allows you to access an attribute in a given class. 
Setter: A method that allows you to set or mutate the value of an attribute in a class.'''


# de studiat cei 4 piloni oop pana pe 17 tema