"""
Multiplikationstabellen
Vi behöver en funktion som kan ge oss multiplikationstabellen.
Parametern "n" talar om vilket tals tabell vi ska skapa.
Parametern "limit" talar om var vi ska sluta.
Om vi till exempel frågar efter 3:ans tabell, med limit==4, ska programmet räkna ut:
3*1 = 3
3*2 = 6
3*3 = 9
3*4 = 12

multiplication_table(3, 4) → [3, 6, 9, 12]

Formulera krav och acceptanskriterier.
Kör sedan red-green-refactor för varje acceptanskriterium.

AK1: If n is less than or equal to 0, return an empty list.
AK2: If limit is less than or equal to 0, return an empty list.
AK3: If n is greater than 0 and limit is greater than 0, return a list of the multiples of n, from n to n*limit.

"""

def muliplication_table(num, limit):
    if num <= 0 or limit <= 0:
        return []
    else:
        return [num * i for i in range(1, limit + 1)]