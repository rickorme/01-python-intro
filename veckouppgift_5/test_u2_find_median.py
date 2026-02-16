
# AK1: If the list is empty, return None.
# AK2: If the list has an odd number of elements, return the middle element after sorting the list.
# AK3: If the list has an even number of elements, return the average of the two middle elements after sorting the list.

from veckouppgift_5.u2_functions import find_median
from pytest import approx

def test_find_median():
    assert find_median([]) is None
    assert find_median([1, 2, 3]) == 2
    assert find_median([1, 2, 1000]) == 2
    assert find_median([1, 2, 3, 4]) == approx(2.5)