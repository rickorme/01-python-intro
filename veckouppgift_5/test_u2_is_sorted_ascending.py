
# AK1: If numbers is an empty list, return False.
# AK2: If numbers has one element, return True.
# AK3: If numbers is sorted in ascending order, return True.
# AK4: If numbers is not sorted in ascending order, return False.

from veckouppgift_5.u2_functions import is_sorted_ascending

def test_is_sorted_ascending():
    assert is_sorted_ascending([]) == False
    assert is_sorted_ascending([1]) == True
    assert is_sorted_ascending([1, 2, 3]) == True
    assert is_sorted_ascending([3, 2, 1]) == False
    assert is_sorted_ascending([1, 2, 2, 3]) == True