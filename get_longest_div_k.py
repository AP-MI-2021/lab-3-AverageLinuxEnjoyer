from get_longest_subsequence import get_longest_subsequence

def are_div_by_k(lst: list[int]) -> bool:
    """Verifica daca numerele dintr-o liste sunt divizibile cu k

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca toate numerele sunt divizibile cu k, False in caz contrar
    """
    for x in lst:
        if x % are_div_by_k.k != 0:
            return False

    return True

def test_are_div_by_k():
    are_div_by_k.k = 6
    assert are_div_by_k([36,6,12,48]) == True

    are_div_by_k.k = 1
    assert are_div_by_k([123,346,123,456745]) == True

    are_div_by_k.k = 23142345
    assert are_div_by_k([0]) == True

    are_div_by_k.k = 129
    assert are_div_by_k([]) == True

    are_div_by_k.k = 16
    assert are_div_by_k([2,3,12,5,9]) == False

test_are_div_by_k()


def get_longest_div_k(lst: list[int], k: int) -> list[int]:
    """Returneaza cea mai lunga subsecventa cu numere divizibile cu k dintr-o lista

    Args:
        lst (list[int]): Lista principala cu toate numerele
        k (int): Numarul cu care este verificata divizibilitatea 

    Returns:
        list[int]: Subsecventa cu numerele divizibile la k
    """
    are_div_by_k.k = k
    return get_longest_subsequence(lst, are_div_by_k)

print()

def test_get_longest_div_k():
    assert get_longest_div_k([12,45,63,29,56,48,32,78,91,115], 2) == [56,48,32,78]
    assert get_longest_div_k([], 6) == []
    assert get_longest_div_k([0],246) == [0]
    assert get_longest_div_k([3,6,123,7,9], 3) == [3,6, 123]

test_get_longest_div_k()


