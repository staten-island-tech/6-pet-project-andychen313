""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(f"{self.name} purchased {item} and has {self.inventory}")
Nathan = Hero("Nathan", 0, ["Pencil"])
print(Nathan.__dict__)
Nathan.buy("Xi Yang") """

""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Jillian = Hero("Jillian", 150, ["Potion"])
print(Jillian.__dict__)

Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__) """

""" class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance +=amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
Andy = BankAccount("Andy", 150)
print(Andy.__dict__) """

""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
    
Andy = Hero("Andy", 100, ["Tree Branch"])
print(Andy.__dict__)

Andy.buy("Sword - atk: 34 dmg")
print(Andy.__dict__) """

class Pet:
    def __init__(self, name, happiness_level):
        self.name = name
        self.__happiness_level = happiness_level
    
    def play(self, amount):
        Game = input("What game is your pet playing?: ")
        print(f"{self.name} is playing {Game}"!)
        self.__happiness_level +=10


    