'''Домашнее задание к лекции 1.7 «Классы и их применение в Python»
Необходимо реализовать классы животных на ферме:

Коровы, козы, овцы, свиньи;
Утки, куры, гуси.
Условия:

Должен быть один базовый класс, который наследуют все остальные животные.
Базовый класс должен определять общие характеристики и интерфейс.'''

class Animals():
    def __init__(self, name, size, paws, hoofs, wings):
        self.name = name
        self.size = size
        self.paws = paws
        self.hoofs = hoofs
        self.wings = wings
        print (self.name, self.size, self.paws, self.hoofs, self.wings)

        def info(self):
            print(self.name, self.size, self.paws, self.hoofs, self.wings)

    def __str__(self):
        return str({
            'name': self.name,
            'size': self.size,
            'paws': self.paws,
            'hoofs': self.hoofs,
            'wings': self.wings,
        })


class Birds(Animals):
    name_bird = ['Утки', 'Куры', 'Гуси']

    def __init__(self, name_bird):
        self.name_bird = name_bird
        Animals.__init__(self, name_bird, 'small', 2, 'None', 'Yes')


class Animal(Animals):
    name_animal = ['Коровы', 'Козы', 'Овцы', 'Свиньи']
    def __init__(self, name_animal):
        self.name_animal = name_animal
        Animals.__init__(self, name_animal, 'big', 4, 'Yes', 'None')
        
class Cows(Animal):
    def __init__(self, name, size, paws, hoofs, wings):
        super().__init__(name, size, paws, hoofs, wings)
        self.hoofs = 4


ducks = Birds('Утки')
chickens = Birds('Куры')
geese = Birds('Гуси')

Cows = Animal('Коровы')
Goats = Animal('Козы')
Sheep = Animal('Овцы')
Pigs = Animal('Свиньи')

# print(Birds._dict_)
print('\n Класс Птицы:',
      '\n Утки: {}'.format(ducks),
      '\n Куры: {}'.format(chickens),
      '\n Гуси: {}'.format(geese))

print('\n Класс Животные:',
      '\n Коровы: {}'.format(Cows),
      '\n Козы: {}'.format(Goats),
      '\n Овцы: {}'.format(Sheep),
      '\n Свиньи: {}'.format(Pigs))
