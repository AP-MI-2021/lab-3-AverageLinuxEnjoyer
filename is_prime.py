from math import sqrt

def is_prime(x: int) -> bool:
    """Verifica daca un numar este prim

    Args:
        x (int): Numarul este prim

    Returns:
        bool: True daca x este prim, False in caz contrar
    """
    if x < 2:
        return False

    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False

    return True

def test_is_prime():
    assert is_prime(17) == True
    assert is_prime(32) == False
    assert is_prime(55) == False
    assert is_prime(0) == False
    assert is_prime(1) == False

test_is_prime()