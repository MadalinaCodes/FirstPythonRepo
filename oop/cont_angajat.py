# tema
# clasa Angajat
# nume, prenume, salariu, vechime
# in constructor punem: nume, prenume, salariu, functie, vechime
# metode
# descriere
# marire salariu in functie de vechime
# actualizare vechime (iau un parametru numit noua vechime)
        # self.vechime = noua_vechime
# mai dati o data o descriere si atunci a mai trecut un an sa zicem
# daca are vechime sub 5 ani, marim cu 300, peste 5 ani, 500
# pe urma mai apelam o data descrierea (rand 6)

class Angajat:
    #constructorul
    def __init__(self, nume, prenume, salariu, functie):
    # atribute, fields
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.functie = functie
        self.vechime = 0

    # metode
    def dateAngajat(self):
        print(f'Nume {self.nume}')
        print(f'Prenume {self.prenume}')
        print(f'Salariu {self.salariu} lei')
        print(f'Funtie {self.functie}')
        print(f'Vechime {self.vechime} ani')
        print('-----------------------------------------------------------')

    def actualizareVechime(self, noua_vechime):
        self.vechime = noua_vechime
        print(f'Vechime angajat {noua_vechime} ani')

    def marireSalariu(self, noua_vechime):
            if noua_vechime >= 5:
                noul_salariu = self.salariu + 500
                self.salariu = noul_salariu
                print(f'Marire salariu cu 500 de lei, noul salariu este de {noul_salariu} lei')
                print('__________________________________________________________________________')
            else:
                noul_salariu = self.salariu + 300
                self.salariu = noul_salariu
                print(f'Marire salariu cu 300 de lei, noul salariu este de {noul_salariu} lei')
                print('__________________________________________________________________________')

