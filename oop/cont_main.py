from oop.cont_bancar import ContBancar

cont1 = ContBancar ('Madalina A', 'RO001')
cont2 = ContBancar ('Bogdan D', 'RO002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300) # 0
cont2.alimentareCont(700)
cont2.alimentareCont(300) # 700

cont1.plataCard(500)
cont1.plataCard(300)
cont2.plataCard(100)
cont2.plataCard(200)

cont1.interogareSold()
cont2.interogareSold()

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
# pe urma mai apelam o data descrierea (rand 27)





