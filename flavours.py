class FlavorCategories:
    tradicional = [
        "Calabresa",
        "Mussarela",
        "Portuguesa",
        "Frango com Catupiry",
        "Quatro Queijos",
        "Margherita",
        "Pepperoni",
        "Atum",
        "Bacon",
        "Vegetariana"
    ]
    especial = [
        "Frango com Cheddar",
        "Palmito",
        "Brócolis com Catupiry",
        "Rúcula com Tomate Seco",
        "Mexicana",
        "Baiana",
        "Caprese",
        "Carbonara",
        "Napolitana",
        "Havaiana"
    ]
    sweet = [
        "Brigadeiro (Pizza doce com chocolate)",
        "Beijinho (Pizza doce com leite condensado e coco)",
        "Banana com Canela",
        "Floresta Negra (Pizza doce com chocolate e cerejas)",
        "Maracujá com Chocolate (Pizza doce com maracujá e chocolate)"
    ]

    additional_toppings = [
        "Calabresa",
        "Bacon",
        "Presunto",
        "Frango",
        "Cebola",
        "Pimentão",
        "Tomate",
        "Azeitona",
        "Milho",
        "Palmito",
        "Cogumelo",
        "Ovo",
        "Rúcula",
        "Queijo Gorgonzola",
        "Queijo Brie",
        "Queijo Cheddar",
        "Queijo Parmesão",
        "Queijo Catupiry",
        "Manjericão",
        "Orégano",
        "Pimenta",
        "Azeite de Oliva",
        "Molho Barbecue",
        "Molho de Pimenta",
        "Molho de Alho",
        "Molho de Tomate",
        "Molho de Queijo",
        "Molho de Ervas",
        "Molho de Mostarda e Mel"
    ]

    def add_pizza_to_category(self, category, pizza):
        if category == 'tradicional':
            self.tradicional.append(pizza)
        elif category == 'especial':
            self.especial.append(pizza)
        elif category == 'sweet':
            self.sweet.append(pizza)
    
    def delete_pizza_from_category(self, category, pizza):
        if category == 'tradicional':
            if pizza in self.tradicional:
                self.tradicional.remove(pizza)
            else:
                print("Pizza not found in the tradicional category!")
        elif category == 'especial':
            if pizza in self.especial:
                self.especial.remove(pizza)
            else:
                print("Pizza not found in the especial category!")
        elif category == 'sweet':
            if pizza in self.sweet:
                self.sweet.remove(pizza)
            else:
                print("Pizza not found in the sweet category!")
        else:
            print("Invalid category!")
        