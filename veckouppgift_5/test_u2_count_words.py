from veckouppgift_5.u2_functions import count_words

def test_count_words():
    assert count_words("") == 0
    assert count_words("Hello") == 1
    assert count_words("Hello world") == 2
    assert count_words("The quick brown fox jumps over the lazy dog") == 9