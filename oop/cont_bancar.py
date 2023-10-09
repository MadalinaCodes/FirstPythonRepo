class ContBancar:
    #constructorul
    def __init__(self, titularCont, iban):
    # atribute, fields
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = True
        self.pin = 7777
        self.incercari_activare = 0

    # metode
    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Nr de incercari {self.incercari_activare}')
        print('_____________________________________________')

    def activareCont(self, pin_utilizator):
            self.salut()
            if pin_utilizator == self.pin:
                print('Card activat')
                self.activ = False
            else:
                print('PIN gresit')
                self.incercari_activare = self.incercari_activare + 1
                # se mai poate pune asa self.incercari_activare+=1

    def alimentareCont(self, suma):
            self.sold +=suma # se ia suma si se adauga la sold
            print(f'Ati alimentat {suma}')

    def plataCard(self, suma):
             # asta se numeste variable scope
            self.salut()
            if suma <= self.sold:
                self.sold -= suma
                print(f'Ati cheltuit {suma}')
                print(f'Aveti in cont {self.sold}')
            else:
                print('Fonduri insuficiente')

    def salut(self):
        print(f'Buna {self.titularCont}')






