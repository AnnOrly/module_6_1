class Animal:
    alive = True # живой
    fed = False # накормленный

    def __init__(self, name_animal):
        self.name_animal = name_animal

    def eat(self, food):
        self.food = food
        if food.edible:
            print(f'{self.name_animal} съел {food.name_plant}')
            self.fed = True
            print('Животное накормлено')
        else:
            print(f'{self.name_animal} не стал есть {food.name_plant}')
            self.alive = False
            print('Животное погибло от голода')

class Mammal(Animal):  # млекопитающие
    pass

class Predator(Animal):  # хищник
    pass


class Plant:
    edible = False # съедобный

    def __init__(self, name_plant):
        self.name_plant = name_plant

class Flower(Plant): # цветы
    pass

class Fruit(Plant): # фрукты
    edible = True



animal_1 = Predator('Кот')
animal_2 = Mammal('Корова')

plant_1 = Flower('Ромашка')
plant_2 = Fruit('Яблоко')


#
#
# animal_2.eat(plant_2)
#
# animal_3.eat(plant_3)
#
# animal_4.eat(plant_4)

print(animal_1.name_animal)
print(plant_1.name_plant)
print(animal_1.alive)
animal_1.eat(plant_1)
print(animal_1.alive)

print('---------------------------')

print(animal_2.name_animal)
print(plant_2.name_plant)
print(animal_2.alive)
animal_2.eat(plant_2)
print(animal_2.alive)