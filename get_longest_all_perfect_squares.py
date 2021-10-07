from math import sqrt
from get_longest_subsequence import get_longest_subsequence

def are_perfect_squares(lst: list[int]) -> bool:
    """Verifica daca o lista este formata doar din patrate perfecte

    Args:
        lst (list[int]): Lista verifiata

    Returns:
        bool: True daca e formata doar din patrate perfecte, False in caz contrar.
    """
    for x in lst:
        if x != int(sqrt(x)) ** 2:
            return False
    
    return True

def test_are_perfect_squares():
    assert are_perfect_squares([]) == True
    assert are_perfect_squares([2,5,36,9]) == False
    assert are_perfect_squares([36,16,36,9,1,0]) == True
    assert are_perfect_squares([49, 64]) == True

test_are_perfect_squares()

def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa a unei liste date, continand doar elementele care sunt patrate perfecte.

    Args:
        lst (list[int]): Lista principala

    Returns:
        list[int]: Subsecventa ta cu patratele perfecte
    """
    return get_longest_subsequence(lst, are_perfect_squares)


def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([23,45,91,81,36,25,6,25,16,58,9]) == [81,36,25]
    assert get_longest_all_perfect_squares([17,21,48]) == []
    assert get_longest_all_perfect_squares([49, 6, 9, 21, 25, 25]) == [25,25]
    assert get_longest_all_perfect_squares([]) == []

test_get_longest_all_perfect_squares()