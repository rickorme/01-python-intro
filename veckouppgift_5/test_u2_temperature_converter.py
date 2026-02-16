from veckouppgift_5.u2_functions import c_to_f
from pytest import approx

def test_c_to_f():
    assert c_to_f(-273.15) == approx(-459.67)
    assert c_to_f(-40) == -40
    assert c_to_f(0) == 32
    assert c_to_f(100) == 212
    assert c_to_f(-274) is None