import pytest

from jdwilliams_utils.math import (
    factorial,
    gcd,
    is_prime,
    lcm,
)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(10) == 3628800
    with pytest.raises(ValueError):
        factorial(-5)

def test_gcd():
    assert gcd(0,0) == 0
    assert gcd(0,2) == 2
    assert gcd(3,0) == 3
    assert gcd(5,5) == 5
    assert gcd(21,35) == 7
    assert gcd(-4,6) == 2
    assert gcd(15,-18) == 3
    assert gcd(-45,-65) == 5

def test_is_prime():
    assert not is_prime(-5)
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(6)
    assert not is_prime(150)

    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(17)
    assert is_prime(97)

def test_lcm():
    assert lcm(0,0) == 0
    assert lcm(0,5) == 0
    assert lcm(7,0) == 0
    assert lcm(4,6) == 12
    assert lcm(21,6) == 42
    assert lcm(-3,5) == 15
    assert lcm(4,-8) == 8
    assert lcm(-7,-3) == 21
