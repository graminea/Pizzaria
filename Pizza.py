from countdown import countdown
from flavours import FlavorCategories
from Client import Client
from Login import Login


class Pizza:
    def __init__(self, size, flavor, extra_toppings=None):
        self.size = size
        self.flavor = flavor
        self.extra_toppings = extra_toppings if extra_toppings else []
        self.price = None

    def get_price(self, pizza_type, size):
        prices = {
            'traditional': {
                'small': 45,
                'medium': 55,
                'large': 65
            },
            'special': {
                'small': 55,
                'medium': 65,
                'large': 75
            },
            'sweet': {
                'small': 50,
                'medium': 60,
                'large': 70
            }
        }
        return prices.get(pizza_type, {}).get(size.lower(), 0)
    
    def total_price(self):
        total_price = self.price + len(self.extra_toppings) * 5
        return total_price

    def description(self):
        if self.size == 'small':
            print("Tamanho: Broto")
        elif self.size == 'medium':
            print("Tamanho: Média")
        else:
            print("Tamanho: Grande")
        
        if self.flavor in FlavorCategories.tradicional:
            self.price = self.get_price('traditional', self.size)
        elif self.flavor in FlavorCategories.especial:
            self.price = self.get_price('special', self.size)
        elif self.flavor in FlavorCategories.sweet:
            self.price = self.get_price('sweet', self.size)
        
        print(self.flavor)
        
        if self.extra_toppings:
            toppings_names = [FlavorCategories.additional_toppings[num - 1] for num in self.extra_toppings]
            print("Extras: ", ', '.join(toppings_names))
        print("Total: R$",self.total_price())

    def order(self, balance):
        print(f"Fazendo o pedido...")
        countdown(2)
        print("Resumo:")
        self.description()
        if balance > self.total_price():
            print("Pizza pedida com sucesso!")
            return True, self.total_price()
        else:
            print('Saldo insuficiente para compra!!')
            print('Adicione saldo para comprar!')
            countdown(2)
            return False, None