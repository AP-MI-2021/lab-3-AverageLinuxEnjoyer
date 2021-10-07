from is_prime import is_prime
from get_longest_subsequence import get_longest_subsequence

def is_sum_prime(lst: list[int]) -> bool:
    """Verifica daca suma elementelor unei liste este prima

    Args:
        lst (list[int]): Lista cu elementele

    Returns:
        bool: True daca suma e prima, False in caz contrar
    """
    sum = 0
    for x in lst:
        sum+=x

    return is_prime(sum)

def test_is_sum_prime():
    assert is_sum_prime([]) == False
    assert is_sum_prime([1,5,7]) == True
    assert is_sum_prime([2]) == True
    assert is_sum_prime([2,3,4,5,9,20,5]) == False

test_is_sum_prime()

def get_longest_sum_is_prime(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa a unei liste in care suma numerelor e prima

    Args:
        lst (list[int]): Lista principala

    Returns:
        list[int]: Subsecventa a carei sume va fi numar prim
    """
    return get_longest_subsequence(lst, is_sum_prime)

def test_get_longest_sum_is_prime():
    assert get_longest_sum_is_prime([12,4,9,2,5,7,1,12]) == [9,2, 5,7]
    assert get_longest_sum_is_prime([20,44,82]) == []
    assert get_longest_sum_is_prime([53,51,44,25,4,3]) == [51, 44, 25, 4, 3]
    assert get_longest_sum_is_prime([25,94,81,7]) == [7]

test_get_longest_sum_is_prime()