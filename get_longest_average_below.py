from get_longest_subsequence import get_longest_subsequence
from typing import Callable

def is_average_below_lambda(average: float) -> Callable:
    """Returneaza o functie lambda care verifica daca media elementelor unei liste e sub o anumita valoare

    Args:
        average (float): Valoarea sub care trebuie sa se afle elementele listei

    Returns:
        Callable: Functia lambda returnata
    """
    return lambda lst: (sum(lst) / len(lst)) < average if len(lst) > 0 else True

def test_is_average_below_lambda():
    assert is_average_below_lambda(10)([7,2,9,8,12]) == True
    assert is_average_below_lambda(24)([]) == True
    assert is_average_below_lambda(2)([0]) == True
    assert is_average_below_lambda(5)([4,2,16,1,3]) == False

test_is_average_below_lambda()

def get_longest_average_below(lst: list[int], average: float) -> list[int]:
    """Returneaza cea mai lunga subsecventa in care media elementelor este sub o anumita valoare

    Args:
        lst (list[int]): Lista principala
        average (float): Valoarea sub care trebuie sa fie media

    Returns:
        list[int]: Subsecventa cu elementele mai mici decat average
    """
    return get_longest_subsequence(lst, is_average_below_lambda(average))

def test_get_longest_average_below():
    assert get_longest_average_below([2,4,12,91,43,5], 9) == [2,4,12]
    assert get_longest_average_below([54,31,29,62], 10) == []
    assert get_longest_average_below([], 5) == []
    assert get_longest_average_below([0, 30], 14) == [0]

test_get_longest_average_below()