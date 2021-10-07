from get_longest_subsequence import get_longest_subsequence
from is_prime import is_prime

def are_not_prime(lst: list[int]) -> bool:
    """Verifica daca o lista e formata doar din numere care nu sunt prime

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca lista e formata doar din numere prime, False in caz contrar
    """
    for x in lst:
        if is_prime(x):
            return False

    return True

def test_are_not_prime():
    assert are_not_prime([23,8,9,17,5]) == False
    assert are_not_prime([]) == True
    assert are_not_prime([0, 4, 27]) == True
    assert are_not_prime([5]) == False

test_are_not_prime()

def get_longest_all_not_prime(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa de numere care nu sunt prime

    Args:
        lst (list[int]): Lista initiala

    Returns:
        list[int]: Subsecventa de numere prime
    """
    return get_longest_subsequence(lst, are_not_prime)

def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([2,4,7,9,21]) == [9,21]
    assert get_longest_all_not_prime([]) == []
    assert get_longest_all_not_prime([2,13,29,31]) == []
    assert get_longest_all_not_prime([15,27,18, 21]) == [15,27,18,21]

test_get_longest_all_not_prime()