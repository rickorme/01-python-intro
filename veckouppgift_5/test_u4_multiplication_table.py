"""
AK1: If n is less than or equal to 0, return an empty list.
AK2: If limit is less than or equal to 0, return an empty list.
AK3: If n is greater than 0 and limit is greater than 0, return a list of the multiples of n, from n to n*limit.
"""
from veckouppgift_5.u4_multiplication_table import muliplication_table


def test_muliplication_table():
    assert muliplication_table(0, 5) == [] # AK1
    assert muliplication_table(-1, 5) == [] # AK1
    assert muliplication_table(5, -1) == [] # AK2
    assert muliplication_table(5, 0) == [] # AK2
    assert muliplication_table(3, 4) == [3, 6, 9, 12] # AK3