import pytest
import sys
sys.path.append("./src")
from gender_utils import parse_gender
"""
Tests to ensure the parse_gender function works as expected.
"""
@pytest.mark.parametrize("text,expected", [
    ("His book is on the table.", ("male", "his")),
    ("Her bag is red.", ("female", "her")),
    ("The doctor finished their work.", ("unknown", None)),
    ("His and her tasks are done.", ("unknown", None)),
    ("  HER coat is new  ", ("female", "her")),
    ("**His** and her tasks are done.", ("unknown", None)),
])
def test_parse_gender(text, expected):
    assert parse_gender(text) == expected

def test_parse_gender_smoke():
    example_texts = [
        "His book is on the table.",
        "Her bag is red.",
        "The doctor finished their work.",
        "His and her tasks are done.",
        "  HER coat is new  ",
        "",
        "No pronoun here.",
        "HIS or HER choice?"
    ]

    for text in example_texts:
        result = parse_gender(text)
        # check that it returns a tuple
        assert isinstance(result, tuple)
        # check that the first element is a string
        assert isinstance(result[0], str)
        # second element is either string or None
        assert result[1] is None or isinstance(result[1], str)