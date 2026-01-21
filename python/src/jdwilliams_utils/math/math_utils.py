def factorial(n: int) -> int:
    """Compute the factorial of a non-negative integer.

    Args:
        n (int): The integer to compute the factorial for.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of two integers using the Euclidean algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    a = abs(a)
    b = abs(b)
    max_val = a if a > b else b
    min_val = a if a < b else b
    while min_val != 0:
        max_val, min_val = min_val, max_val % min_val
    return max_val

def is_prime(n: int) -> bool:
    """
    Return True if the given integer is a prime number.

    A prime number is an integer greater than 1 that has no positive
    divisors other than 1 and itself.
    """
    if n < 2:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    limit = int(n**0.5) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def lcm(a: int, b: int) -> int:
    """Compute the least common multiple of two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The least common multiple of a and b.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

