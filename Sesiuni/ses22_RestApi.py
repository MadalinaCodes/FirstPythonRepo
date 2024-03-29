"""https://simple-books-api.glitch.me/orders/
https://github.com/vdespa/introduction-to-postman-course
https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md"""

import requests
import json
class BooksApiClient:
    base_url = "https://simple-books-api.glitch.me"

    def __init__(self, name, email, token=""):
        self.name = name
        self.email = email
        self.token = token
        if self.token == "":
            self.token = self.__authentication()


    def __authentication(self):
        url = f"{self.base_url}/api_clients"
        body = {
            "clientName": self.name,
            "clientEmail": self.email
        }
        headers = {
            "contentType": "application/json"
        }
        response = requests.post(
            url=url,
            headers=headers,
            data=json.dumps(body)
        )
        print(url)
        response = requests.post(url=url, data=json.dumps(body))
        print(response.json())
        return response.json()['accessToken']

    def get_orders(self):
        # get request base_url + "orders"
        url = f"{self.base_url}/orders"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url=url, headers=headers)
        return response.json()

    def get_books(self):
        # get request catre base_url + "books"
        pass

    def submit_order(self):
        pass

    def delete_order(self):
        pass

client = BooksApiClient(
    name="madalina",
    email="madalina@gmail.com",
    token="d7bac69cfcf52059858676ca6353016bec7b8f3f3796ff9cd2a03077603c5263"
)

print(client.get_orders())
