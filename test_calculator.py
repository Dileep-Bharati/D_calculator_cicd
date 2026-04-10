import pytest
from calculator import add, subtract, multiply, divide, power, modulus, squareroot

def test_add():
    assert add(2, 3) == 5
    assert add (-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3,4) == 12 #fix wrong multiplication for testing CI/CD

def test_divide():
    assert divide(10,2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)

def test_power():
    assert power(2,3) == 8

def test_modulus():
    assert modulus(10,3) == 1

def test_squareroot():
    assert squareroot(9) == 3.0   # √9 = 3.0
    assert power(2, 3) == 8   # 2³ = 8

def test_modulus():
    assert modulus(10, 3) == 1

def test_squareroot():
    assert squareroot(9) == 3.0   # √9 = 3.0
