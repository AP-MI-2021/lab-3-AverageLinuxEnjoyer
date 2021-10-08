from get_longest_subsequence import get_longest_subsequence


def are_in_arithmetic_progression(lst: list[int]) -> bool:
    """Verifica daca elementele unei liste sunt in progresie aritmetica

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca sunt in progresie, False in caz contrar
    """
    if len(lst) <= 2:
        return True

    last_dif = lst[1] - lst[0]
    for i in range(2, len(lst)):

        dif = lst[i] - lst[i-1]

        if dif != last_dif:
            return False

        last_dif = dif

    return True

def test_are_in_arithmetic_progression():
    assert are_in_arithmetic_progression([1,2,3,4,5]) == True
    assert are_in_arithmetic_progression([-5,10,25]) == True
    assert are_in_arithmetic_progression([5,12,49,81]) == False
    assert are_in_arithmetic_progression([]) == True

test_are_in_arithmetic_progression()

def get_longest_arithmetic_progression(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa a unei liste in care numerele sunt in progresie aritmetica

    Args:
        lst (list[int]): Lista principala

    Returns:
        list[int]: Subsecventa cu numere in progresie aritmetica
    """
    return get_longest_subsequence(lst, are_in_arithmetic_progression)
