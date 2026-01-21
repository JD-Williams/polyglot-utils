def capitalize(value: str | None) -> str | None:
    """
    Capitalizes the first character of the string and lowercases the rest.

    Args:
        value (str | None): The string to capitalize.
    """
    if value is None or value == "":
        return value
    return value[0].upper() + value[1:].lower()

def equals_nullable(a: str | None, b: str | None) -> bool:
    """
    Compares two strings for equality, handling None values.

    Args:
        a (str | None): The first string.
        b (str | None): The second string.
    """
    return (a or "") == (b or "")

def is_blank(value: str | None) -> bool:
    """
    Returns True if the string is None, empty, or contains only whitespace.

    Args:
        value (str | None): The string to check.
    """
    return value is None or value.strip() == ""

def normalize_whitespace(value: str | None) -> str | None:
    """
    Normalizes whitespace in the string by stripping leading/trailing whitespace
    and replacing multiple consecutive whitespace characters with a single space.

    Args:
        value (str | None): The string to normalize.
    """
    if value is None:
        return None
    return ' '.join(value.split())

def truncate(value: str | None, max_length: int, suffix: str | None = "") -> str | None:
    """
    Truncates the string to a maximum length, appending a suffix if truncation occurs.

    Args:
        value (str | None): The string to truncate.
        max_length (int): The maximum allowed length of the string.
        suffix (str | None): The suffix to append if truncation occurs.
    """
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if value is None or len(value) <= max_length:
        return value
    return value[:max_length - len(suffix)] + suffix
