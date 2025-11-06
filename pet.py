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

""" class Pet:
    def __init__(self, name, happiness_level):
        self.name = name
        self.__happiness_level = happiness_level
    
    def play(self, amount: int):
        self.__happiness_level = 0
        amount = 10
        self.__happiness_level +=amount
        print(f"Sean is playing and gained {amount} happiness.")
Sean = Pet("Sean", 0)
print(Sean.__dict__) """

""" class Pet:
    def __init__(self, name, happinesslevel):
        self.name = name
        self.__happinesslevel__ = happinesslevel

    def play(self, game, amountgain):
        self.__happinesslevel__ +=amountgain
        print(f"Sean played {game} and now has {self.__happinesslevel__} happiness.")


Sean = Pet("Sean", 0)
Sean.play("with a frisbee", 10) """

class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.__money__ = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Jillian = Hero("Jillian", 150, ["Potion"])
print(Jillian.__dict__)

Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__)