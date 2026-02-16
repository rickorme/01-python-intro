"""
AK1: If input is an empty string, return an empty list.
AK2: If no elements in master_list, return an empty list.
AK3: If input is not an empty string, return a list of all elements in master_list that start with input. The comparison should be case-insensitive.
AK4: If input is not an empty string, return a list of all elements in master_list that contain input, sorted first by those names which start with input, 
        then by alphabetical order. The comparison should be case-insensitive.
"""
from veckouppgift_5.u3_autocomplete_list import autocomplete_list


def test_autocomplete_list():
    full_list = ["Alice", "Bob", "Charlie", "Mark", "Marianne", "Marlene", "Mary", "Arlene", "Arianne", "Arnold", "Carl"]

    assert autocomplete_list("", full_list) == [] # AK1
    assert autocomplete_list("X", []) == [] # AK2
    assert autocomplete_list("Mar", full_list) == ["Marianne", "Mark", "Marlene", "Mary"] # AK3
    assert autocomplete_list("ar", full_list) == ["Arianne", "Arlene", "Arnold", "Carl", "Charlie", "Marianne", "Mark", "Marlene", "Mary"] # AK4