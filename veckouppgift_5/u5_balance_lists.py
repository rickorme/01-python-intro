
"""
Balansera listor
Som en del i ett större program har vi en lista som kan innehålla flera element. 
Men elementen kan flyttas mellan denna och en annan lista. 
Vi behöver ett sätt att balansera listorna, så att de har lika många element - åtminstone så nära som möjligt. 
Ordningen på elementen är inte viktig.

Formulera krav och acceptanskriterier.

Kör sedan red-green-refactor för varje acceptanskriterium.

AK1: If both lists are empty, return two empty lists.
AK2: If one list is empty and the other has an even number of elements, move elements from the non-empty list to the empty list 
    until both lists have the same number of elements
AK3: If one list is empty and the other has an odd number of elements, move elements from the non-empty list to the empty list 
    until the length of the lists differ by at most one element.
AK4: If both lists have elements, move elements from the longer list to the shorter list 
    until both lists have the same number of elements or differ by at most one element.

"""
def balance_lists(list1, list2):
    if not list1 and not list2:
        return 0, 0
    elif not list1:
        while len(list2) > len(list1) +1:
            list1.append(list2.pop())
    elif not list2:
        while len(list1) > len(list2) +1:
            list2.append(list1.pop())
    else:
        list1_start_len = len(list1)
        list2_start_len = len(list2)
        can_balance_equally = (list1_start_len - list2_start_len) % 2 == 0
        modifier = 0 if can_balance_equally else 1

        if list1_start_len > list2_start_len:
            while len(list1) > len(list2) + modifier:
                list2.append(list1.pop())
        elif list2_start_len > list1_start_len:
             while len(list2) > len(list1) + modifier:
                list1.append(list2.pop())

    return len(list1), len(list2)