"""
AK1: If both lists are empty, return two empty lists.
AK2: If one list is empty and the other has an even number of elements, move elements from the non-empty list to the empty list 
    until both lists have the same number of elements
AK3: If one list is empty and the other has an odd number of elements, move elements from the non-empty list to the empty list 
    until the length of the lists differ by at most one element.
AK4: If both lists have elements, move elements from the longer list to the shorter list 
    until both lists have the same number of elements or differ by at most one element.

"""
from veckouppgift_5.u5_balance_lists import balance_lists

def test_balance_lists():
    assert balance_lists([], []) == (0, 0) # AK1
    assert balance_lists([], [1, 2, 3, 4]) == (2, 2) # AK2
    assert balance_lists([], [1, 2, 3]) == (1, 2) # AK3
    assert balance_lists([1, 2, 3, 4], []) == (2, 2) # AK2
    assert balance_lists([1, 2, 3], []) == (2, 1) # AK3
    assert balance_lists([1, 2], [3, 4, 5, 6]) == (3, 3) # AK4
    assert balance_lists([1, 2, 3, 4], [5, 6]) == (3, 3) # AK4
    assert balance_lists([1, 2], [3, 4, 5, 6, 7]) == (3, 4) # AK4
    assert balance_lists([1, 2, 3, 4, 5], [5, 6]) == (4, 3) # AK4