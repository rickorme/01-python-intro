# 1 Vilka ekvivalensklasser har uttrycken?
# 1a. x > 100   
# 1b. y == 42
# 1c. len(text) >= 5
# 1d. z == True
# 1e. 8 < v < 16
# 1f. w == 32 or w == 64 or w == 128
# 1g. if x < 5: … elif x < 10: … elif x < 15: … else

# 1a "<= 100" and "> 100
# 1b "not equal to 42" and "equal to 42"
# 1c "shorter than 5 characters" and "5 or more characters"
# 1d "Not True" och "True"
# 1e "berween 9 and 15", "less than or equal to 9" and "greater than or equal to 16"
# 1f "w is 32, 64 or 128" and "w is not 32, 64 or 128"
# 1g "x is less than 5", "x is between 5 and 9", "x is between 10 and 14" and "x is 15 or greater"


# 2 Det har smugit sig in kommentarer i stället för kod på några ställen. 
# Skriv färdigt testfallen test_empty_list och test_number_list.
# Returnerar summan av alla tal i listan
def sum_list(list):
    return sum(list)

def test_empty_list():
    expected = 0
    actual   = sum_list([])
    assert actual == expected
    
def test_number_list():
    # testa med listor som har ett, två respektive fem element.
    assert sum_list([5]) == 5
    assert sum_list([5, 10]) == 15
    assert sum_list([1, 2, 3, 4, 5]) == 15


# 3a Diskutera följande kod. Ett testfall räcker inte för att testa funktionen - föreslå fler testfall, som täcker in alla olika möjligheter för count_vowels.
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
# Tips 1: kan funktionen hitta någon vokal, över huvud taget?
# Tips 2: kan den räkna alla vokaler?
# Tips 3: kan den räkna samma vokal om den förekommer flera gånger?
# Tips 4: klarar den både stora och små bokstäver?
def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
    count = 0
    for vowel in vowels:
        count += word.lower().count(vowel)
    return count

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0
    assert count_vowels("aeiouyåäö") == 9
    assert count_vowels("AEIOUYÅÄÖ") == 9
    assert count_vowels("aAeEiIoOuUyYåÅäÄöÖ") == 18
    assert count_vowels("aAeE vvtt iIoO 9788 uU ppplll yYåÅäÄöÖ") == 18

# 3b Skriv färdigt funktionen count_vowels med hjälp av TDD-metoden, red → green → refactor.


# 4 Formulera testfall för en funktion som hittar största talet i en lista.
# Returnerar det största talet i listan
# Returnerar None om det inte finns något
def find_max(list):    
    if not list:
        return None
    
    highest = max(list)
    return highest

def test_find_max():
    assert find_max([]) == None
    assert find_max([5]) == 5
    assert find_max([5, 10]) == 10
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-1, -2, -3, -4, -5]) == -1

# 5 Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite heder åt alla andrapristagare. 
# Formulera testfall för en funktion som hittar näst största talet i en lista!
# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet
def find_2nd_max(list):    
    if not list:
        return None
    
    highest = max(list)
    highest_count = list.count(highest)

    if len(list) == highest_count:
        return highest
    else:
        list = [x for x in list if x != highest]
        second_highest = max(list)
        return second_highest


def test_find_2nd_max():
    assert find_2nd_max([]) == None
    assert find_2nd_max([5]) == 5
    assert find_2nd_max([5, 10]) == 5
    assert find_2nd_max([1, 2, 3, 4, 5]) == 4
    assert find_2nd_max([-1, -2, -3, -4, -5]) == -2
    assert find_2nd_max([5, 5]) == 5
    assert find_2nd_max([5, 5, 4]) == 4
    assert find_2nd_max([5, 5, 4, 3]) == 4