from get_longest_subsequence import get_longest_subsequence
from is_prime import is_prime

def is_concat_prime(lst: list[int]) -> bool:
    """Verifica daca concatenarea numerelor dintr-o lista formeaza un numar prim

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca concatenarea formeaza numar prim, False in caz contrar
    """
    if len(lst) == 0:
        return True

    return is_prime(int("".join([str(x) for x in lst])))

def test_is_concat_prime():
    assert is_concat_prime([1,8,77]) == True
    assert is_concat_prime([]) == True
    assert is_concat_prime([4,82,5,9,6,3]) == True
    assert is_concat_prime([1,6]) == False

test_is_concat_prime()

def get_longest_concat_is_prime(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa a unei liste in care concatenarea numerelor formeaza un numar prim

    Args:
        lst (list[int]): Lista principala

    Returns:
        list[int]: Subsecventa care respecta proprietatea
    """
    return get_longest_subsequence(lst, is_concat_prime)

def test_get_longest_concat_is_prime():
    assert get_longest_concat_is_prime([4,8,5,9,6,4]) == [8,5,9]
    assert get_longest_concat_is_prime([4,82,65,96]) == []
    assert get_longest_concat_is_prime([1, 14, 25, 17]) == [17]
    assert get_longest_concat_is_prime([]) == []

test_get_longest_concat_is_prime()