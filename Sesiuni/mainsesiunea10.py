from datetime import date
from sesiunea10 import Om

om1 = Om('Madalina', 0, 3, date.today())
om2 = Om('Rares', 0, 3, date.today())
om3 = Om('Gina', 0, 3, date.today())
om4 = Om('Ion', 0, 3, date.today())

numar = str(10) # str este functie a lui int

maternitate = [om1, om2, om3, om4]

for element in maternitate:
    element.print_self()

print(om1)
print(om2)
print(om3)
print(om4)

print(maternitate)