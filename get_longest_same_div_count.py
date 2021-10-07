from get_longest_subsequence import get_longest_subsequence
from math import sqrt

def get_number_of_divisors(n: int) -> int:
    """Returneaza numarul de divizori al unui numar

    Args:
        n (int): Numarul verificat

    Returns:
        int: Numarul de divizori
    """
    divisors = {1,n}
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)

    return len(divisors)

def test_get_number_of_divisors():
    assert get_number_of_divisors(36) == 9
    assert get_number_of_divisors(100) == 9
    assert get_number_of_divisors(0) == 2
    assert get_number_of_divisors(97) == 2

test_get_number_of_divisors()

def all_same_divisors(lst: list[int]) -> bool:
    """Verifica daca elementele unei liste au acelasi numar de divizori

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca au acelasi numar de divizori, False in caz contrar
    """
    for i in range(1, len(lst)):
        if get_number_of_divisors(lst[i]) != get_number_of_divisors(lst[i-1]):
            return False
        
    return True

def test_all_same_divisors():
    assert all_same_divisors([36,100]) == True
    assert all_same_divisors([]) == True
    assert all_same_divisors([2, 97, 13, 0]) == True
    assert all_same_divisors([0,14,59,21]) == False

test_all_same_divisors()


def get_longest_same_div_count(lst: list[int]) -> list[int]:
    """Returneaza cea mare lunga subsecventa cu numere care au acelasi numar de divizori

    Args:
        lst (list[int]): Lista principala

    Returns:
        list[int]: Subsecventa
    """
    return get_longest_subsequence(lst, all_same_divisors)

def test_get_longest_same_div_count():
    assert get_longest_same_div_count([1,14,92,36,100]) == [36,100]
    assert get_longest_same_div_count([5,3,17,51,97]) == [5,3,17]
    assert get_longest_same_div_count([]) == []
    assert get_longest_same_div_count([36,81,45,2]) == [36]

test_get_longest_same_div_count()