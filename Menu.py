from Pizza import Pizza
from Client import Client
from flavours import FlavorCategories
from Login import Login 
from countdown import countdown
import json
import sys

def Menu(username, login_manager, client):
    if login_manager.logins[login_manager.index_logged_user]["adm"]: #ve se o usuario é admin (funcionario)
        balance = login_manager.get_balance(username) #atualiza o saldo sempre que da uma volta no loop
        print('--------------------------------------------LOGIN COMO ADMIN------------------------------------------')
        print()
        print('Digite a opção desejada: ')
        print('1. Adicionar saldo')
        print('2. Ver saldo')   
        print('3. Ver Catálogo')
        print('4. Pedir pizza')
        print('5. Ver suas Pizzas')
        print('6. Ver logins')
        print('7. Adicionar sabor de Pizza')
        print('8. Excluir Pizza')
        print('0. Encerrar programa')
        option = int(input("Escolha uma opção: ")) #variavel para escolher da tab
    else:
        balance = login_manager.get_balance(username)
        print('--------------------------------------BEM VINDO A SAGÁS PIZZARIA--------------------------------------')
        print()
        print('Digite a opção desejada: ')
        print('1. Adicionar saldo')
        print('2. Ver saldo')   
        print('3. Ver Catálogo')
        print('4. Pedir pizza')
        print('5. Ver suas Pizzas')
        print('0. Encerrar programa')
        option = int(input("Escolha uma opção: "))


    if option == 0:
        sys.exit(0) #exit funcion 
    
    if option == 1: #adiciona saldo
        while True:
            amount = float(input("Digite o valor que deseja adicionar: "))
            if 0 < amount < 1000:
                countdown(1)
                client.add_balance(amount) #chamando as funcoes de Cliente 
                client.get_balance()  
                countdown(1) #funcao para 'atrasar' o codigo e deixar mais limpo o terminal
                print()
                break
            else:
                print('Valor muito alto ou zero não foi aceito, tente novamente!')
                countdown(2)
    elif option == 2: #verifica o saldo
        countdown(1)
        client.get_balance() #chamando as funcoes de Cliente
        countdown(1)
        print()

    elif option == 3: #ver o catálogo
        print("Catálogo de Sabores:")
        print('------------------------------------------------------------------------------------------------------')
        countdown(1)
        print("Tradicionais:")
        print()
        countdown(2)
        for i, flavor in enumerate(FlavorCategories.tradicional, start=1): #printa cada pizza de determinada categoria
            print(f"{i}. {flavor}")
        print('------------------------------------------------------------------------------------------------------')
        print("Especiais:")
        print()
        countdown(2)
        for i, flavor in enumerate(FlavorCategories.especial, start=1): #printa cada pizza de determinada categoria
            print(f"{i}. {flavor}")
        print('------------------------------------------------------------------------------------------------------')
        print("Doces:")
        print()
        countdown(2)
        for i, flavor in enumerate(FlavorCategories.sweet, start=1): #printa cada pizza de determinada categoria
            print(f"{i}. {flavor}")
        print('------------------------------------------------------------------------------------------------------')
        countdown(3)

    elif option == 4: #comprar a pizza
        print('Entrando no sistema...')
        countdown(1)
        print()
        print('1.Broto')
        print('2.Média')
        print('3.Grande')
        while True:
            countdown(1)
            print()
            choice_size = int(input('Digite a opção desejada: ')) #escolher tamanho
            if 0 < choice_size <= 3: #verificar se não esta fora dos parametros
                if choice_size == 1:
                    size = 'small'
                elif choice_size == 2:
                    size = 'medium'
                else:
                    size = 'large'
                break
            else:
                print('Tamanho incorreto, digite novamente!')
                countdown(1)
                print()
        print()
        countdown(1)
        print('1. Tradicional (R$ 45 Broto, R$55 Média, R$65 Grande)')
        print('2. Especial (R$ 55 Broto, R$65 Média, R$75 Grande)')
        print('3. Doce (R$ 50 Broto, R$60 Média, R$70 Grande)')
        while True:
            countdown(1)
            print()
            choice_type = int(input('Digite a opção: ')) #escolher o tipo
            countdown(1)
            print()
            if 0 < choice_type <= 3: #verificar se não esta fora dos parametros
                if choice_type == 1:
                    for i, flavor in enumerate(FlavorCategories.tradicional, start=1):
                        print(f"{i}. {flavor}")
                    while True:
                        countdown(1)
                        print()
                        choice_flavor = int(input('Digite a pizza desejada: ')) #escolher o numero da pizza dentre as pizzas mostradas pelo enumarate
                        if 0 < choice_flavor <= len(FlavorCategories.tradicional): #verificar se não esta fora dos parametros
                            choice_flavor = FlavorCategories.tradicional[choice_flavor - 1] #achar na lista o sabor escolhido
                            break
                        else:
                            print('Número incopatível, tente novamente!')
                            countdown(1)
                elif choice_type == 2:
                    for i, flavor in enumerate(FlavorCategories.especial, start=1): 
                        print(f"{i}. {flavor}")
                    while True:
                        countdown(1)
                        print()
                        choice_flavor = int(input('Digite a pizza desejada: ')) #escolher o numero da pizza dentre as pizzas mostradas pelo enumarate
                        if 0 < choice_flavor <= len(FlavorCategories.especial): #verificar se não esta fora dos parametros
                            choice_flavor = FlavorCategories.especial[choice_flavor - 1] #achar na lista o sabor escolhido
                            break
                        else:
                            print('Número incopatível, tente novamente!')
                            countdown(1)
                else:
                    for i, flavor in enumerate(FlavorCategories.sweet, start=1):
                        print(f"{i}. {flavor}")
                    while True:
                        countdown(1)
                        print()
                        choice_flavor = int(input('Digite a pizza desejada: ')) #same
                        if 0 < choice_flavor <= len(FlavorCategories.sweet): #same
                            choice_flavor = FlavorCategories.sweet[choice_flavor - 1] #same
                            break
                        else:
                            print('Número incopatível, tente novamente!')
                            countdown(1)
                break
            else:
                print('Número incopatível, tente novamente!')
                countdown(1)
        
        countdown(1)
        print()
        adicional_if = input('Deseja algum adicional? (S/N): ').upper() #verificar se o cliente quer adicionais
        if adicional_if == 'S': #verificacao
            print('Cada Adicional custa R$5') 
            countdown(2)
            print()
            toppings = FlavorCategories.additional_toppings #chamar a lista de adicionais
            half = len(toppings) // 2 #dividir em duas colunas para melhor vizualizacao no terminal
            first_column = list(enumerate(toppings[:half], start=1)) 
            second_column = list(enumerate(toppings[half:], start=half + 1))

            for top1, top2 in zip(first_column, second_column): #print das duas colunas e o zip faz um de cada vez simuntaneo
                print(f"{top1[0]}. {top1[1]:<20}", end='')  #"<20" representa a largura do print"
                if top2:
                    print(f"{top2[0]}. {top2[1]}")
                else:
                    print()
            adicionais = input('Digite o número dos adicionais separados por um espaço: ').split(' ') #verificar o numero de adicionais (5 para cada)
            pizza_order = Pizza(size, choice_flavor, [int(num) for num in adicionais]) #instanciacao da classe Pizza
            success, price = pizza_order.order(balance) #chamar o order method para fazer a compra
            countdown(4)
        else:
            print('Sem Adicional!')
            pizza_order = Pizza(size, flavor) #instanciacao da classe Pizza
            success, price = pizza_order.order(balance) #chamar o order method para fazer a compra
            countdown(4)
        
        if success: #se o saldo for suficiente...
            client.update_balance(price) #atualiza o saldo do cliente
            client.add_pizza(pizza_order) #adiciona a pizza a lista de pizza do cliente

    elif option == 5:
        countdown(1)
        print('Lista das suas pizzas') #lista das pizzas ja compradas
        print()
        pizza_list = client.get_pizza_list() #chama o metodo de pegar as listas
        if pizza_list:
            for i, pizza in enumerate(pizza_list, start=1): #enumarate cada pizza (se tiver mais que uma)
                print(f'Pizza {i}:')
                pizza.description()
                countdown(3)
                print() 

        else:
            print("You haven't ordered any pizzas yet.")
        countdown(5)

    elif option == 6:
        if login_manager.logins[login_manager.index_logged_user]["adm"]: #verifica se e adm 
            login_manager.get_logins('logins.json') #pega todos os logins
            print('Loaded Logins:')
            countdown(1)
            for login in login_manager.logins:
                print(f'Usuário: {login["user"]:<15} senha: {login["password"]:<15} saldo: R${login["balance"]}') #print de todos os logins com width alterado para melhor vizializacao no terminal
            countdown(3)

    elif option == 7:
        while True:
            print('Escolha o tipo da pizza a ser adicionada')
            print('1. Tradicional') 
            print('2. Especial' )
            print('3. Doce ')
            category = int(input('Digite o tipo de pizza que deseja adicionar: ')) #escolhe a categoria da pizza a ser adicionada
            if 0 < category <= 3:
                if category == 1:
                    category = 'tradicional'
                elif category == 2:
                    category = 'especial'
                else:
                    category = 'sweet'
                break
            else:
                print('Numero invalido, tente novamente!!')

        pizza = input('Digite o nome da pizza: ') #nome da pizza
        pizzatest = FlavorCategories() #instanciacao da classe FlavorCategories
        pizzatest.add_pizza_to_category(category, pizza) #uso do metodo de adicionar pizzas


    elif option == 8:
        while True:
            print('Escolha o tipo da pizza a ser excluída')
            print('1. Tradicional') 
            print('2. Especial' )
            print('3. Doce ')
            category = int(input('Digite o tipo de pizza que deseja excluir: '))
            
            if 0 < category <= 3:
                if category == 1:
                    category_name = 'tradicional'
                    category_list = FlavorCategories.tradicional
                elif category == 2:
                    category_name = 'especial'
                    category_list = FlavorCategories.especial
                else:
                    category_name = 'sweet'
                    category_list = FlavorCategories.sweet
                break
            else:
                print('Número inválido, tente novamente!!')

        print(f"Escolha a pizza a ser excluída da categoria {category_name}:")
        for i, flavor in enumerate(category_list, start=1):
            print(f"{i}. {flavor}")

        while True:
            pizza_index = int(input('Digite o número da pizza a ser excluída: '))
            if 0 < pizza_index <= len(category_list):
                pizza_name = category_list[pizza_index - 1]
                break
            else:
                print('Número inválido, tente novamente!')

        
        FlavorCategories().delete_pizza_from_category(category_name, pizza_name) #uso do metodo de adicionar pizzas
        print(f'Pizza {pizza_name} deletada')

    




    else: 
        print('Opção invalida') #opcao invalida retorna ao tab de opcoes
        countdown(3)

