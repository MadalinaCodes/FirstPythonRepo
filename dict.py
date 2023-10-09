lista_goala = []
dict_gol = {}

# declaram si initializam un map
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}

# adaugam elemente
note_elevi ['Sebi'] = 7

# printam dictul
print(note_elevi)

# aflam elementul
print(note_elevi['Gigel'])
print(note_elevi.get('Gigel'))

# actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

# aflam dimensiunea
print(len(note_elevi))

# sterg valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'nu mai avem acest elev'))
print(note_elevi)

# returneaza doar cheile
print(note_elevi.keys())