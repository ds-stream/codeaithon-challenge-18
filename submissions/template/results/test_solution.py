import pytest
from solution import reverse_substrings

def test_single_word():
    assert reverse_substrings("hello") == "olleh"

def test_multiple_words():
    assert reverse_substrings("hello world") == "olleh dlrow"

def test_empty_string():
    assert reverse_substrings("") == ""

def test_palindrome_words():
    assert reverse_substrings("madam racecar level") == "madam racecar level"

def test_sentence_with_punctuation():
    assert reverse_substrings("hello, world!") == ",olleh !dlrow"

def test_spaces_between_words():
    assert reverse_substrings("  hello   world  ") == "  olleh   dlrow  "

def test_single_character_words():
    assert reverse_substrings("a b c") == "a b c"

if __name__ == "__main__":
    pytest.main()
