# DJANGO vine cu un ORM (cum e SQL Alchemy)
# prin DJANGO poti face filtrele pentru date cum sunt filtrele de pe emag cand vrei sa restrangi rezultatele.

# exemplu de comanda in SQL
'''select * from products
where products.category == telefoane'''

# ce este un API?

import requests
from pprint import pprint

url = "https://jsonplaceholder.typicode.com/users/1/todos?completed=true"
parameters = {
    "completed": "true"
}

response = requests.get(url=url, params=parameters)

pprint(response.json())


class Todo:
    url = "https://jsonplaceholder.typicode.com/users/1/todos/"

    def get_all(self):
        pass

    def filter_todo(self, parameters):
        pass

class

my_todo_list = Todo()
my_todo_list.get_all()


'''Corneliu Mihai Gherman10:49
class Todo:
    url = 'https://jsonplaceholder.typicode.com/users/1/todos'

    def get_all(self):
        response = requests.get(self.url)
        return response.text

    def filter(self, parameters):
        response = requests.get(self.url, params=parameters)
        return response.text'''