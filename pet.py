class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(f"{self.name} purchased {item} and has {self.inventory}")
Nathan = Hero("Nathan", 0, ["Pencil"])
print(Nathan.__dict__)
Nathan.buy("Xi Yang")