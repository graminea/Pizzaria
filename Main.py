from Pizza import Pizza
from Client import Client
from flavours import FlavorCategories
from Login import Login 
from countdown import countdown
from Menu import Menu
import json
import sys

def main(): #Inicia o código
    login_manager = Login() #instancia os logins
    login_manager.login() #=====
    username = login_manager.logged_user #chama o username do login para fazer o cliente
    client = Client(username) #instancia o cliente
    while True:
        Menu(username, login_manager, client) #inicia o menu

main()


