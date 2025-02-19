class Animal:
    def __init__(self, name, cry, color, species, age):
        self.__name = name 
        self.__cry = cry
        self.__color = color
        self.__species = species
        self.__age = age
        
    def name(self):
        print("This animal is a", self.__name) 

    def cry(self):
        print("It makes the sound", self.__cry)

    def color(self):
        print("The color of the animal is", self.__color) 

    def species(self):
        print("The animal's species is", self.__species)

    def age(self):
        print("The animal is", self.__age, "years old")

