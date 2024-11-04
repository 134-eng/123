class Pet:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.energy = 100

    def play(self):
        if self.energy >= 10:
            print(f"{self.name} грається")
            self.energy -= 10
        else:
            print(f"{self.name} дуже втомлений щоб грати")
        
    def feed(self):
        print(f"{self.name} ситий")
        self.energy += 10
        if self.energy > 100:
            self.energy = 100

    def sleep(self):
        print(f"{self.name} спить")
        self.energy = 100

    def get_info(self):
        return f"ім'я: {self.name},вік: {self.age}, енергія: {self.energy}"

    def grow_older(self):
        self.age += 1


my_pet = Pet("барсик")


print(my_pet.get_info())
my_pet.play()
my_pet.feed()
my_pet.sleep()
my_pet.grow_older()