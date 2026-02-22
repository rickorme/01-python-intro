"""
2 Länder

1a På Island bor det 383726 invånare och i Danmark 5961249. Skapa objekt för länderna. (Data från januari 2024. Avrunda befolkningen.)
class Country:
    def __init__(self, name, pop):
        self.__name = name
        self.__population = pop

se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)

1b Lägg till en metod med namnet "print_info". Om man anropar den för Sverige-objektet ska den skriva ut: "I Sverige bor det 10.5 miljoner invånare". 
Metoder ska använda klassens egenskaper, så att den fungerar för de andra länderna och inte bara för Sverige.

1c Lägg till landets area som en egenskap till klassen. Använd en parameter till konstruktorn, alltså __init__ metoden. 
Ge arean ett default värde på None så att man inte måste ange arean när man skapar ett landsobjekt.
Exempel på default värde för en vanlig funktion:
# y har default värde 10
def exempel(x, y=10):
    print(x + y)

exempel(2)  # skriver ut 12

1d Ändra i metoden "print_info" så att den skriver ut arean också, men bara om arean inte är None.

1e Skapa en ny metod med namnet "add_language". Den ska lägga till ett av landets officiella språk. 
(Sverige har bara ett, men Finland har två språk (svenska och finska) och Schweiz har fyra.) 
För att kunna spara ett varierande antal behöver du använda en lista.

1f Ändra i "print_info" så att den skriver ut alla officiella språk, på en ny rad.
"""

class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area  
        self.__languages = []

    def add_languages(self, languages):        
        if isinstance(languages, list):
            self.__languages.extend(languages)
        else:
            self.__languages.append(languages)

    def print_info(self):
        info = f"\nIn {self.__name} there are {self.__population} milion inhabitants."
        if self.__area is not None:
            info += f"\nThe area is {self.__area} square kilometers."
        if len(self.__languages) > 0:
            info += f"\nOfficial languages: {', '.join(self.__languages)}."
        print(info)

se = Country("Sweden", 10.5, 450295)
no = Country("Norway", 5.5, 385207)
dk = Country("Denmark", 5.96, 42933)
iceland = Country("Iceland", 0.38, 103000)
fi = Country("Finland", 5.5, 338455)

se.print_info()
se.add_languages(["Swedish"])
se.print_info()

fi.print_info()
fi.add_languages(["Swedish", "Finnish"])
fi.print_info()