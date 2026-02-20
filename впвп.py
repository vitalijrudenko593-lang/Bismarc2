class Pet:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.hunger = 50
        self.energy = 50
        self.mood = 50
    def eat(self):
        self.hunger = max(0, self.hunger - 20)
        self.mood = min(100, self.mood + 10)
        print(f"{self.name} поїв 🥣")

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.hunger = min(100, self.hunger + 10)
        print(f"{self.name} поспав 😴")

    def play(self):
        if self.energy < 20:
            print(f"{self.name} занадто втомлений для гри 😕")
        else:
            self.energy -= 20
            self.hunger += 15
            self.mood = min(100, self.mood + 20)
            print(f"{self.name} грається 🎾")

    def status(self):
        print(f"""
Ім'я: {self.name}
Тип: {self.kind}
Голод: {self.hunger}
Енергія: {self.energy}
Настрій: {self.mood}
""")