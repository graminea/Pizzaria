from countdown import countdown
import time
import json


class Login:
    def __init__(self):
        self.logins = []  
        self.userslist = []
        self.variable = 1  
        self.index_logged_user = None

        self.get_logins('logins.json') #load the previous logins from the json file

    #do the login
    def login(self): 
        while self.variable == 1:
            print('\nBem Vindo a Sagás Pizzaria ')
            h = input('Você tem cadastro? (S/N): ').upper()
            if h == 'S':
                print('LOGIN.', end='')
                for i in range(2):
                    print('.', end='', flush=True)
                    countdown(1)
                
                user = input('\nDigite o usuário: ')
                password = input('Digite a senha: ')
                for i in range(len(self.logins)):
                    if self.logins[i]['user'] == user and self.logins[i]['password'] == password:
                        self.logged_user = user
                        self.index_logged_user = i  
                        self.variable = 0
                        print('Login efetuado com sucesso!!')
                        print('Entrando.', end='')
                        for i in range(2):
                            print('.', end='', flush=True)
                            countdown(1)
                        print()
                        break
                else:
                    print('Usuário ou senha incorretos!!')
                    print('Faça o login novamente!!')
                    print()
                    continue

            else:
                x = input('Deseja fazer o cadastro? (S/N): ').upper()
                if x == 'S':
                    self.login_make()

    #make a username and passoword to access 
    def login_make(self):
        user = input('Crie um usuário: ')
        password = input('Crie uma senha: ')
        self.logins.append({'user': user, 'password': password, 'balance': 0, 'adm': False})
        self.userslist.append(user)
        print('Usuário criado com sucesso!')
        print('Realize o login para continuar.', end='')
        for _ in range(2):
            print('.', end='', flush=True)
            countdown(1)

        self.save_logins('logins.json') #save the new login
        print()

    def get_balance(self, username):
        try:
            with open('logins.json', 'r') as file:
                self.logins = json.load(file)
                for login in self.logins:
                    if login['user'] == username:
                        return login['balance']
                return None  # Return None if the username is not found
        except FileExistsError:
            return None
    
    def get_logins(self, name): #method to get all the saved logins in the json file
        try:
            with open(name, 'r') as file:
                self.logins = json.load(file)
                self.userslist = [login['user'] for login in self.logins]
        except FileNotFoundError:
            print("Arquivo de logins não encontrado. Criando um novo.")

    def save_logins(self, name): #the save login method
        with open(name, 'w') as file:
            json.dump(self.logins, file)
    
    




        
