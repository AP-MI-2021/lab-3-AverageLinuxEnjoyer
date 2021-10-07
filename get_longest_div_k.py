from get_longest_subsequence import get_longest_subsequence
from typing import Callable

def are_div_by_k_lambda(k: int) -> Callable:
    """Returneaza o functie lambda care verifica divizibilitatea tuturor elementelor unei liste la un numar dat

    Args:
        k (int): Numarul dat mai departe functiei lambda

    Returns:
        Callable: Functia lambda returnata
    """
    
    return lambda lst: all(x % k == 0 for x in lst)

def test_are_div_by_k_lambda():
    assert are_div_by_k_lambda(6)([36,6,12,48]) == True

    assert are_div_by_k_lambda(1)([123,346,123,456745]) == True

    assert are_div_by_k_lambda(23142345)([0]) == True

    assert are_div_by_k_lambda(129)([]) == True

    assert are_div_by_k_lambda(16)([2,3,12,5,9]) == False

test_are_div_by_k_lambda()

def get_longest_div_k(lst: list[int], k: int) -> list[int]:
    """Returneaza cea mai lunga subsecventa cu numere divizibile cu k dintr-o lista

    Args:
        lst (list[int]): Lista principala cu toate numerele
        k (int): Numarul cu care este verificata divizibilitatea 

    Returns:
        list[int]: Subsecventa cu numerele divizibile la k
    """
    return get_longest_subsequence(lst, are_div_by_k_lambda(k))

def test_get_longest_div_k():
    assert get_longest_div_k([12,45,63,29,56,48,32,78,91,115], 2) == [56,48,32,78]
    assert get_longest_div_k([], 6) == []
    assert get_longest_div_k([0],246) == [0]
    assert get_longest_div_k([3,6,123,7,9], 3) == [3,6, 123]

test_get_longest_div_k()


