from Login import Login
from countdown import countdown
import time

class Client(Login):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.pizza_list = []

    def get_balance(self):
        for login in self.logins:
            if login['user'] == self.username:
                print(f"Saldo: R${login['balance']}")
                return login['balance']
        print("User not found.")
        return None

    def add_balance(self, amount):
        for login in self.logins:
            if login['user'] == self.username:
                login['balance'] += amount
                print(f"Saldo de R${amount} adicionado.")
                self.save_logins('logins.json')
                return login['balance']
        print("User not found.")
        return None

    def update_balance(self, amount):
        for login in self.logins:
            if login['user'] == self.username:
                login['balance'] -= amount
                print(f"Novo saldo: R${login['balance']}.")
                self.save_logins('logins.json')
    
    def add_pizza(self, pizza):
        self.pizza_list.append(pizza)
        print("Para acessar suas pizzas digite 5 no menu")
        countdown(1)

    def get_pizza_list(self):
        return self.pizza_list
    









