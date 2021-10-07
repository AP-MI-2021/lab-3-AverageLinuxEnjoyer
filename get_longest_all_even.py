from get_longest_subsequence import get_longest_subsequence

def are_even(lst: list[int]) -> bool:
    """Verifica daca toate elementele unei liste sunt numere pare

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca toate elementele sunt pare, False in caz contrar
    """
    for x in lst:
        if x % 2 == 1:
            return False

    return True

def test_are_even():
    assert are_even([2,4,6,8]) == True
    assert are_even([]) == True
    assert are_even([1,2,3,4]) == False
    assert are_even([1]) == False

test_are_even()

def get_longest_all_even(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa in care toate elementele sunt numere pare

    Args:
        lst (list[int]): Lista principala

    Returns:
        list[int]: Subsecventa cu numere pare
    """
    return get_longest_subsequence(lst, are_even)

def test_get_longest_all_even():
    assert get_longest_all_even([1,2,3,4,5,6,8,9,10]) == [6,8]
    assert get_longest_all_even([1,5,7,9,12]) == [12]
    assert get_longest_all_even([]) == []
    assert get_longest_all_even([1,5,13]) == []

test_get_longest_all_even()