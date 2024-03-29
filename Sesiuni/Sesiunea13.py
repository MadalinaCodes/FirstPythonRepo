# Cerinte miniproiect  B .... merge codul

# TODO LIST
#     Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
#
# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
# finalizează_task(nume) - se va sterge din dict
# afișează_todo_list() - doar cheile
# afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
# Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
# Dacă acesta răspunde nu - la revedere
# Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict


class TodoList:
    """todo este un dictionar cu chei si valori pt aceste chei
    cheile sunt unice"""
    todo = {}

    def afiseaza_todo(self):
        for items in self.todo:
            print(items)

    def adauga_task(self, nume_task, descriere_task):
        self.todo[nume_task] = descriere_task

    def finalizeaza_task(self, nume_task):
        self.todo.pop(nume_task)

    def detalii_suplimentare(self, nume_task):
        '''
        this method displays details about tasks
        :param nume_task: this is the key of our todo dictionary
        :return: nothing
        '''
        # verificam daca nume_task este in self.todo si il adaugam daca nu este

        if nume_task not in self.todo:
            response = input('taskul nu este in todo. vrei sa il adaugi? (da/nu)')
            if response == 'da':
                descriere = input('introdu descriere task: ')
                self.adauga_task(nume_task, descriere)
            else:
                print(self.todo[nume_task])

        print(self.todo[nume_task])

todo_list = TodoList()
todo_list.afiseaza_todo()
todo_list.adauga_task('learn python1', 'doing python exercises')
todo_list.adauga_task('learn python2', 'doing python gfsdjs')
todo_list.adauga_task('learn python3', 'doing python akjdha')
todo_list.afiseaza_todo()
todo_list.detalii_suplimentare('learn java')

todo_list.afiseaza_todo()