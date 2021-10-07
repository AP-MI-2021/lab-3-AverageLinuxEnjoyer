from get_longest_subsequence import get_longest_subsequence

def is_product_odd(lst: list[int]) -> bool:
    """Verifica daca produsul elementelor unei liste e numar impar

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca produsul e impar, False in caz contrar 
    """
    product = 1
    for x in lst:
        product *= x

    return product % 2 == 1

def test_is_product_odd():
    assert is_product_odd([3,3,3,3,3]) == True
    assert is_product_odd([2,2,2,2,2]) == False
    assert is_product_odd([]) == True
    assert is_product_odd([2,3,4,5]) == False

test_is_product_odd()

def get_longest_product_is_odd(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa al carei elemente inmultite dau un numar impar

    Args:
        lst (list[int]): Lista principala

    Returns:
        list[int]: Subsecventa cu produsul elementelor impar
    """
    return get_longest_subsequence(lst, is_product_odd)

def test_get_longest_product_is_odd():
    assert get_longest_product_is_odd([1,3,3]) == [1,3,3] 
    assert get_longest_product_is_odd([2,4,6,8]) == []
    assert get_longest_product_is_odd([1]) == [1]
    assert get_longest_product_is_odd([0]) == []

test_get_longest_product_is_odd()