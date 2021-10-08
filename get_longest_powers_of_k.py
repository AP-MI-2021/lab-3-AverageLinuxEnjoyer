from typing import Callable
from get_longest_subsequence import get_longest_subsequence


def can_be_written_x_to_k(n: int, k: int) -> bool:
    """Verifica daca un numar n poate fi scris ca si un intreg la o putere

    Args:
        n (int): Numarul verificat
        k (int): Puterea

    Returns:
        bool: True daca indeplineste conditia, False in caz contrar
    """
    x = 0
    while True:
        if x**k == n:
            return True
        elif x**k > n:
            return False

        x+=1

def test_can_be_written_x_to_k():
    assert can_be_written_x_to_k(8,3) == True
    assert can_be_written_x_to_k(0, 243) == True
    assert can_be_written_x_to_k(1, 13) == True
    assert can_be_written_x_to_k(5,2) == False

test_can_be_written_x_to_k()

def can_all_be_written_x_to_k_lambda(k: int) -> Callable:
    """Returneaza o functie lambda care verifica daca numerele dintr-o lista pot fi scrise ca un intreg la o putere k data

    Args:
        k (int): Puterea

    Returns:
        bool: [description]
    """
    return lambda lst: all(can_be_written_x_to_k(x, k) for x in lst)


def get_longest_powers_of_k(lst: list[int], k: int) -> list[int]:
    """Returneaza cea mai lunga subsecventa in care elementele pot fi scrise ca un intreg la o putere k data

    Args:
        lst (list[int]): Lista principala
        k (int): Puterea

    Returns:
        list[int]: Subsecventa care indeplineste conditia
    """
    return get_longest_subsequence(lst, can_all_be_written_x_to_k_lambda(k))

def test_get_longest_powers_of_k():
    assert get_longest_powers_of_k([8,29,27,64,53],3) == [27,64]
    assert get_longest_powers_of_k([1,2,3,4,5], 1) == [1,2,3,4,5]
    assert get_longest_powers_of_k([], 5) == []
    assert get_longest_powers_of_k([5,6,29,31,43,81], 4) == [81]

test_get_longest_powers_of_k()