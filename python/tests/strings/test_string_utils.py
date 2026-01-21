import pytest

from jdwilliams_utils.strings import (
    capitalize,
    equals_nullable,
    is_blank,
    normalize_whitespace,
    truncate,
)


def test_capitalize():
    assert capitalize(None) is None
    assert capitalize("") == ""
    assert capitalize("hello") == "Hello"
    assert capitalize("hELLO") == "Hello"
    assert capitalize("HELLO") == "Hello"

def test_equals_nullable():
    assert equals_nullable(None, None)
    assert not equals_nullable(None, "not none")
    assert equals_nullable("string", "string")
    assert not equals_nullable("string", "different")

def test_is_blank():
    assert is_blank(None)
    assert is_blank("")
    assert is_blank("   ")
    assert not is_blank("not blank")

def test_normalize_whitespace():
    assert normalize_whitespace(None) is None
    assert normalize_whitespace("") == ""
    assert normalize_whitespace("   ") == ""
    assert normalize_whitespace("  multiple   spaces  ") == "multiple spaces"
    assert normalize_whitespace("leading and trailing   ") == "leading and trailing"

def test_truncate():
    assert truncate(None, 13) is None
    assert truncate("short", 13) == "short"
    assert truncate("this is a long string", 10, "...") == "this is..."
    with pytest.raises(ValueError):
        truncate("This should throw an error", -5)
