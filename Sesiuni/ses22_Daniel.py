import requests
import json

class BooksApiClient:
    base_url = "https://simple-books-api.glitch.me"

    def __init__(self, name, email, token=""):
        self.name = name
        self.email = email
        self.token = token
        if self.token == "":
            self.token = self.__authenticate()

    def __authenticate(self):
        url = f"{self.base_url}/api-clients"
        body = {
            "clientName": self.name,
            "clientEmail": self.email
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(
            url=url,
            headers=headers,
            data=json.dumps(body)
        )
        print(response.json())
        return response.json()

    def get_orders(self):
        # get request base_url + "orders"
        url = f"{self.base_url}/orders"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url=url, headers=headers)

        return response.json()

    def get_books(self):
        # get request catre base_url + "books
        pass

    def submit_order(self, book_id):
        pass

    def delete_order(self, order_id):
        pass


client = BooksApiClient(
    name="3dandan",
    email="3dandan@gmail.com",
    token="990c95b56c9edbcb5737e4f34c64983e594bd7df9291b301f29f42a5fb5fb6e5"
)

print(client.get_orders())

