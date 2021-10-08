from is_prime import is_prime
from get_longest_subsequence import get_longest_subsequence


def only_prime_digits(n: int) -> bool:
    """Verifica daca un numar are toate cifrele prime

    Args:
        n (int): Numarul verificat

    Returns:
        bool: True daca are toate cifrele prime, False in caz contrar
    """
    while n:
        if not is_prime(n % 10):
            return False
        n //= 10

    return True


def test_only_prime_digits():
    assert only_prime_digits(5573) == True
    assert only_prime_digits(238) == False
    assert only_prime_digits(0) == True
    assert only_prime_digits(275) == True


test_only_prime_digits()


def are_list_prime_digits(lst: list[int]) -> bool:
    """Verifica daca toate numerele unei liste sunt formate din cifre prime

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca toate numerele au toate cifrele prime, False in caz contrar
    """
    for x in lst:
        if not only_prime_digits(x):
            return False

    return True


def test_are_list_prime_digits():
    assert are_list_prime_digits([557, 23, 752]) == True
    assert are_list_prime_digits([]) == True
    assert are_list_prime_digits([51, 21]) == False
    assert are_list_prime_digits([28, 49, 51, 23]) == False

test_are_list_prime_digits()

def get_longest_prime_digits(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa in care numerele sunt formate din cifre prime

    Args:
        lst (list[int]): Lista principala

    Returns:
        list[int]: Subsecventa
    """
    return get_longest_subsequence(lst, are_list_prime_digits)


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([41,98,333,27,53,72, 45, 81]) == [333,27,53,72]
    assert get_longest_prime_digits([]) == []
    assert get_longest_prime_digits([1]) == []
    assert get_longest_prime_digits([41,82,53,98,62]) == [53]

test_get_longest_prime_digits()
