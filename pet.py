#Lessons

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

""" class Hero:
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
print(Jillian.__dict__) """

""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.__money__ = money
        self.inventory = inventory

    def buy(self, item, cost):
        self.inventory.append(item)
        self.__money__ -= cost
        print(f"Jillian bought a(n) {item} and now has {self.__money__}.")
Jillian = Hero("Jillian", 150, ["Potion"])
Jillian.buy("sword", 20) """

""" class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"

class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

    def display_info(self):
        return f"Student: {self.name}, Student ID: {self.student_id}"

class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}"
    
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role

    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}"
    
    
student = Student("Alice", "alice@example.com", "S12345")
teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
administrator = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())
print(teacher.display_info())
print(administrator.display_info())

class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role

    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def manage_system(self):
        return f"{self.name} ({self.role}) is managing the system."
admin = Administrator("Ms. Johnson", "johnson@example.com", "Principal")
print(admin.manage_system())

class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Subject: {self.subject}"
    
my_teacher = Teacher("Mr. Brown", "brown@example.com", "Science")
print(my_teacher.display_info()) """

#Pet Project

""" class User:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def display_info(self):
        return f"User: {self.name}, Rank: {self.rank}"
    
class Hunter(User):
    def __init__(self, name, rank, type):
        super().__init__(name, rank)
        self.type = type
    def display_info(self):
        return f"Hunter: {self.name}, Rank: {self.rank}, Type: {self.type}"
    
class Pet(User):
    def __init__(self, name, rank, type):
        super().__init__(name, rank)
        self.type = type
    def display_info(self):
        return f"Shadow: {self.name}, Rank: {self.rank}, Type: {self.type}"
hunter = Hunter("Sung Jin-Woo", "S-Rank", "Shadow Monarch")
pet = Pet("Igros", "A-Rank", "Shadow Soldier")
print(hunter.display_info())
print(pet.display_info())

class ShadowPet(Pet):
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def active(self, activity, level_increase):
        self.level += level_increase
        print(f"{self.name} is {activity} and currently has level {self.level}.")
shadow_pet = ShadowPet("Igros", 10)
shadow_pet.active("battling", 5) """

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.cleanliness = 50
    
    def feed(self):
        self.hunger += 10
        if self.hunger > 100:
            self.hunger = 100
        if self.hunger < 0:
            self.hunger = 0
        if self.hunger >=70:
            print(f"{self.name} is quite full right now!")
        elif self.hunger <= 30:
            print(f"{self.name} is quite hungry! Feed him/her!")
    
    def play(self):
        self.happiness +=10
        if self.happiness > 100:
            self.happiness = 100
        if self.happiness < 0:
            self.happiness = 0
        if self.happiness >= 70:
            print(f"{self.name} is quite happy right now!")
        elif self.happiness <=30:
            print(f"{self.name} is quite sad! Play with him/her!")
    
    def clean(self):
        self.cleanliness +=10
        if self.cleanliness > 100:
            self.cleanliness = 100
        if self.cleanliness < 0:
            self.cleanliness = 0
        if self.cleanliness >=70:
            print(f"{self.name} is quite clean right now!")
        elif self.cleanliness <= 30:
            print(f"{self.name} is quite dirty! Clean him/her!")
    
    def status(self):
        print(f"{self.name} - Hunger: {self.hunger}, Happiness: {self.happiness}, Cleanliness: {self.cleanliness}")
    
    def user_play(self, interaction):
        if interaction == 
    


        
        
