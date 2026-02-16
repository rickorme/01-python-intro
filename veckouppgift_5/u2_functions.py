# 1a Hitta på lämplig testdata till följande funktion, som omvandlar grader Celsius till grader Fahrenheit.
"""
Celsius | Fahrenheit
----------------------
-273.15 | -459.67
-40     | -40
0       | 32
100     | 212
"""
# 1b Vilka ekvivalensklasser har parametern degree?
# "degree is less than -273.15", "degree is equal to -273.15" and "degree is greater than -273.15"

# 1c Skriv ett testfall.

def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32



"""
2a Betrakta funktionen count_words(sentence), som tar en sträng och returnerar antalet ord. Ett ord är en serie tecken som separeras av mellanslag. 
Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.

AK1: If sentence is an empty string, return 0.
AK2: If the sentence contains words, return the number of words in the sentence. Words are separated by spaces.

2b Skriv testfall som testar alla AK.

2c Implementera funktionen, så att alla testfall blir gröna.
"""
def count_words(sentence):
    if sentence == "":
        return 0
    return len(sentence.split())

"""
3a Betrakta funktionen find_median(numbers), som tar en lista med tal och returnerar medianen. 
Median är det mittersta talet, t.ex. är medianen 2 för listan [1, 2, 1000]. 
Om listan har jämnt antal element ska funktionen returnera medelvärdet av de två mittersta talen.
Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.

AK1: If the list is empty, return None.
AK2: If the list has an odd number of elements, return the middle element after sorting the list.
AK3: If the list has an even number of elements, return the average of the two middle elements after sorting the list.

3b Skriv testfall som testar alla AK.

3c Implementera funktionen, så att alla testfall blir gröna.
"""
def find_median(numbers):
    # median = None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers) 
    if n == 0:
        return None
    elif n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    return median

"""
4 Betrakta funktionen is_sorted_ascending(numbers). Den ska returnera True om listan numbers är sorterad i stigande ordning, False annars.
4a Vilka ekvivalensklasser har numbers?

Equivalence classes: 
"numbers is an empty list"
"numbers has one element"
"numbers is sorted in ascending order"
"numbers is not sorted in ascending order"

4b Formulera krav och acceptanskriterier för funktionen.

AK1: If numbers is an empty list, return False.
AK2: If numbers has one element, return True.
AK3: If numbers is sorted in ascending order, return True.
AK4: If numbers is not sorted in ascending order, return False.

4c Skriv testfall för funktionen.
"""
def is_sorted_ascending(numbers):
    # return True

    if len(numbers) == 0:
        return False
    else:
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                return False
        return True
