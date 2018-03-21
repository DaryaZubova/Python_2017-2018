class Animal:
    """
    Hierarchy
    ---------

                 Animal
               /        \\
           Carnivora    Bird
          /     |    \\
    Felidae  Canidae  Ursidae
                |
         (obj)Doge

    """
    def __init__(self, identification, mass, length):
        self.identification = identification
        self.mass = mass
        self.length = length

    def __str__(self):
        return "Type: {}\nID: {}\nMass: {}\nLength: {}\n----".format(self.__class__.__name__,
                                                                     self.identification,
                                                                     self.mass, self.length)

    def __repr__(self):
        return self.__str__()


class Carnivora(Animal):

    __doc__ = Animal.__doc__

    def __init__(self, cannibal, identification, mass, length):
        Animal.__init__(self, identification, mass, length)
        self.cannibal = cannibal

    def __str__(self):
        super_str = super().__str__()
        super_str += "\nCannibal: {}".format(self.cannibal)
        return super_str


class Bird(Animal):
    def __init__(self, number_of_wings, identification, mass, length):
        Animal.__init__(self, identification, mass, length)
        self.number_of_wings = number_of_wings

    def __str__(self):
        super_str = super().__str__()
        super_str += "\nWings: {}".format(self.number_of_wings)
        return super_str


class Felidae(Carnivora):

    __doc__ = "Class for cats and something like that.\n" + Carnivora.__doc__

    def __init__(self, eat_fish, cannibal, identification, mass, length):
        Carnivora.__init__(self, cannibal, identification, mass, length)
        self.eat_fish = eat_fish

    def __str__(self):
        super_str = super().__str__()
        super_str += "\nFish: {}".format(self.eat_fish)
        return super_str


class Canidae(Carnivora):

    __doc__ = "Class for dogs.\n" + Carnivora.__doc__

    def __init__(self, is_wild, cannibal, identification, mass, length):
        Carnivora.__init__(self, cannibal, identification, mass, length)
        self.is_wild = is_wild

    def __str__(self):
        super_str = super().__str__()
        super_str += "\nWild: {}".format(self.is_wild)
        return super_str


class Ursidae(Carnivora):

    __doc__ = "Class for bears.\n" + Carnivora.__doc__

    def __init__(self, is_torpid, cannibal, identification, mass, length):
        Carnivora.__init__(self, cannibal, identification, mass, length)
        self.is_torpid = is_torpid

    def __str__(self):
        super_str = super().__str__()
        super_str += "\nTorpid: {}".format(self.is_torpid)
        return super_str


doge = Canidae(False, False, 'Doge', 15.0, 1.0)
print(doge)
print('')

colibri = Bird(2, 'Colibri', 0.2, 0.1)
print(colibri)


class Zoo:
    """
    Class for zoo with 'useful' methods.
    """
    def __init__(self, open_hour, close_hour):
        self.animals = list()
        self.open_hour = open_hour
        self.close_hour = close_hour

    def add_animal(self, animal):
        self.animals.append(animal)

    def is_closed(self, time):
        return not(self.open_hour <= time and time <= self.close_hour)

    def num_of_dogs(self):
        dogs = list(filter(lambda x: isinstance(x, Canidae), self.animals))
        return len(dogs)

    def num_of_animals(self):
        return len(self.animals)


print('')
print('Set opening hours for zoo: 10:00 - 19:00')

z = Zoo(1000, 1900)  # 1000 == 10:00, 1900 == 19:00

z.add_animal(colibri)
z.add_animal(doge)

print('Is zoo closed at 11:30? - ', z.is_closed(1130))
print('Is zoo closed at 19:03? - ', z.is_closed(1903))

print('Total number of animals - ', z.num_of_animals())
print('Total number of dogs - ', z.num_of_dogs())
