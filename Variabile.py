# variabila = zona din memoria unui calculator care tine date
# variabila = cutie in care punem valori

# am declarat si initializat variabila marca
marca_masina = 'Volkswagen'
model_masina = 'Golf 5 plus'

# nu putem sa punem spatiu in numele variabilei
# o variabila incepe cu litera mica

# loosely typed - nu trebuie sa specificam tipurile de date

print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul: {model_masina}')

# suprascriere
model_masina = 'Golf 6'

print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul: {model_masina}')
# f vine de la format string
nume = 'Andon'
prenume = 'Madalina'
varsta = 27
print(prenume+' '+nume)
print(f'{prenume} {nume} are varsta de {varsta}')
