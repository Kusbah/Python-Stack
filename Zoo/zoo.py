class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.happiness = 50
    def display_info(self):
        print(f"{self.name} (Age: {self.age}), Happiness: {self.happiness}")
    def feed(self):
        self.happiness += 10
        print(f"{self.name} has been feed.")
class Lion(Animal):
    def __init__(self, name, age, roar):
        super().__init__(name, age)
        self.roar = roar
    def feed(self):
        self.happiness += 5
        print(f"{self.name} the lion is happily roaring after being fed!")
class Monkey(Animal):
    def __init__(self, name, age, favoriteToy):
        super().__init__(name, age)
        self.favoriteToy = favoriteToy
    def feed(self):
        self.happiness += 15  
        print(f"{self.name} the monkey jumps around joyfully after eating!")
class Bear(Animal):
    def __init__(self, name, age, furThickness):
        super().__init__(name, age)
        self.furThickness = furThickness
    def feed(self):
        self.happiness += 10
        print(f"{self.name} the bear munches slowly and seems content.")
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to {self.name} Zoo!")
    def feed_all(self):
        print("\nFeeding all animals...")
        for animal in self.animals:
            animal.feed()
    def show_all_animals(self):
        print(f"\n{self.name} Zoo Animal List:")
        for animal in self.animals:
            animal.display_info()
simba = Lion("Simba", 5, "Loud")
george = Monkey("George", 3, "Rubber Banana")
baloo = Bear("Baloo", 7, "Very Thick")
my_zoo = Zoo("Happy Paws")
my_zoo.add_animal(simba)
my_zoo.add_animal(george)
my_zoo.add_animal(baloo)
my_zoo.show_all_animals()
my_zoo.feed_all()
my_zoo.show_all_animals()