'''
1 Skriv en funktion som tar en sträng som parameter. När den anropas ska den skriva ut strängen och "är en fena på programmering". Exempel:
my_function("David") → "David är en riktig hacker"
'''
def who_is_a_hacker(someone: str):
    print(f"{someone} is a proper hacker! 👻")


'''
2a Skriv en funktion med namnet "eko". När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet. Exempel:
eko("hej") → skriver ut "hejhej"
'''
def eko(repeat_word: str):
    print(repeat_word*2)


'''
2b Lägg till en parameter "count", som avgör hur många ekon som ska skapas. Exempel:
eko("hej", 3) → skriver ut "hejhejhej"
'''
def eko2(repeat_word: str, repeat_count: int):
    print(repeat_word*repeat_count)


# 3 Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och justera den enligt kommentaren.
def my_multiplier():
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == end:
            break
    print(y)


'''
4 Skriv en funktion med namnet last. Den ska ta en lista som parameter och returnera det sista elementet i listan.
last([1, 2, 3]) → 3
'''
def last(input_list):
    return input_list[-1]

'''
5 Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, 
där den har tagit bort första och sista elementet
cut_edges([1, 2, 3, 4]) → [2, 3]
'''
def cut_edges(input_list):
    output_list = input_list[1:-1]
    return output_list

'''
6 Lös felen i koden.
'''
def increase(x):
    x += 1
    return x

'''
7 Bygg en funktion med namnet average. 
Den ska ta parametrar: x och y. Båda ska vara tal. 
Funktionen ska returnera medelvärdet. 
Till exempel så räknar man ut medelvärdet av 4 och 8 genom med formeln: (4 + 8) / 2, vilket blir 6.
'''
def average(number1, number2):
    result = (number1 + number2) / 2
    return result

'''
8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. 
Först ska funktionen tala om ifall listan är tom, eller hur många element den har. 
Sedan ska funktionen skriva ut elementen i en punktlista. Exempel:
pretty_print(["a", "b", 3.14])
Listan har 3 element:
1. a
2. b
3. 3.14
'''
def pretty_print_list(input_list):
    index = 0
    list_length = len(input_list)
    pretty_list_result = ""

    if list_length == 0:
        pretty_list_result = "The list is empty"
    else:
        pretty_list_result = f"The list has {list_length} elements:"
        for i in input_list:
            index += 1
            pretty_list_result += f"\n{index}. {i}"

    print(pretty_list_result)