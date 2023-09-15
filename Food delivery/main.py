class Restaurant:
    def __init__(self, name, id, address, location):
        self.name = name
        self.id = id
        self.address = address
        self.location = location
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)

    def delete_food(self, food_name):
        found = False
        for food in self.menu:
            if food.name == food_name:
                self.menu.remove(food)
                found = True
        
        if not found:
            print(f"Could not find {food_name} in the menu.")
            
    def add_food(self, food):
        self.menu.pop(food)


class Food:
    def __init__(self, type, name, price, vegeterian, gluten_free):
        self.type = type
        self.name = name
        self.price = price
        self.vegeterian = vegeterian
        self.gluten_free = gluten_free        

def galvena_programma():
    rest1 = Restaurant("Vairāk saules", 1, "Domina shopping", (50.1234, 49.123))

    rest1.add_food(Food("Starter", "Spring rolls", 4.00, True, True))
    rest1.add_food(Food("Salad", "Cezar", 8.50, False, True))
    rest1.add_food(Food("Main", "Burger", 12.00, True, False))

    rest1.delete_food("Zupa")
    
    print(len(rest1.menu))


galvena_programma()