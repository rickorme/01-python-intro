"""
2a Vad gör följande kod? Fixa eventuella fel.

 - 1) Create a class called Animal with a method make_noise that prints "Detta djur har vi inget ljud för."
 - 2) Create a class called Dog that inherits from Animal and overrides the make_noise method to print "Voff!"
    FIX: the print statement needs to be indented inside the method
 - 3) Create a class called Cat that inherits from Animal and overrides the make_noise method to print "Mjau!"
    it also calls the make_noise method of the parent class to print the default message before printing "Mjau!"
    FIX1: the method parameter should be 'self' instead of 'shelf'
    FIX2: The call to the parent class's make_noise method should be removed - it is not necessary to call the parent method in this case
    , as we want to override it completely.
 - 4) Create a function called sound_off that takes an animal as a parameter and calls its make_noise method.
- 5) Create instances of Cat, Dog, and Rooster (which is not defined in the code) and call the sound_off function with each of them.
    FIX1: The Rooster class is not defined in the code, so we need to either define it or remove it from the list of animals to test.
    FIX2: The sound_off function shuold be modified to accept a list of animals and call make_noise for each animal in the list, instead of just one animal.

"""
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")

class Cat(Animal):
    def make_noise(shelf):
        # super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    def make_noise(self):
        print("Kuckeliku!")

class Cow(Animal):
    def make_noise(self):
        print("Muuu!")        

def sound_off(animal):
    for a in animal:
        a.make_noise()

c = Cat()
d = Dog()
h = Rooster()
k = Cow()
sound_off([c, d, h, k])
