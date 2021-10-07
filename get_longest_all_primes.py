from is_prime import is_prime
from get_longest_subsequence import get_longest_subsequence

def are_numbers_prime(lst: list[int]) -> bool:
    """Verifica daca o lista este formata doar din numere prime

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca toate numerele din lista sunt prime, False in caz contrar
    """
    for x in lst:
        if not is_prime(x):
            return False

    return True

def test_are_numbers_prime():
    assert are_numbers_prime([1,2,5,6]) == False
    assert are_numbers_prime([17, 13, 2, 7]) == True
    assert are_numbers_prime([]) == True
    assert are_numbers_prime([97]) == True

test_are_numbers_prime()

def get_longest_all_primes(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa a unei liste, continand toate elementele numere prime

    Args:
        lst (list[int]): Lista principala

    Returns:
        list[int]: Subsecventa cu elementele prime
    """
    return get_longest_subsequence(lst, are_numbers_prime)

def test_get_longest_all_primes():
    assert get_longest_all_primes([1,7,3,5,14,98,97]) == [7,3,5]
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([1,8,9]) == []
    assert get_longest_all_primes([5,5,5,9,8,5,5]) == [5,5,5]

test_get_longest_all_primes()