from get_longest_subsequence import get_longest_subsequence

def int_equal_to_fractional(n: float) -> bool:
    """Verifica daca partea intreaga a unui numar este egala cu partea sa fractionara

    Args:
        n (float): Numarul verificat

    Returns:
        bool: True daca partea intreaga este egala cu cea fractionara, False in caz contrar
    """
    x = str(n).split('.')
    return x[0] == x[1]

def test_int_equal_to_fractional():
    assert int_equal_to_fractional(47.83) == False
    assert int_equal_to_fractional(0.0) == True
    assert int_equal_to_fractional(893.893) == True
    assert int_equal_to_fractional(98.23) == False

test_int_equal_to_fractional()

def are_int_equal_to_fractional(lst: list[float]) -> bool:
    """Verifica daca fiecare element al unei liste are partea intreaga egala cu partea fractionara

    Args:
        lst (list[float]): Lista verificata

    Returns:
        bool: True daca fiecare element respecta conditia, False in caz contrar
    """
    for x in lst:
        if not int_equal_to_fractional(x):
            return False

    return True

def test_are_int_equal_to_fractional():
    assert are_int_equal_to_fractional([52.52,41.41,0.0]) == True
    assert are_int_equal_to_fractional([]) == True
    assert are_int_equal_to_fractional([43.23,54.89,23.63,85.88]) == False
    assert are_int_equal_to_fractional([1.1]) == True

test_are_int_equal_to_fractional()

def get_longest_equal_int_real(lst: list[float]) -> list[float]:
    """Returneaza cea mai lunga subsecventa in care numerele au partea intreaga egala cu partea fractionara

    Args:
        lst (list[float]): Lista principala

    Returns:
        list[float]: Subsecventa cu numere ce indeplinesc conditia
    """
    return get_longest_subsequence(lst, are_int_equal_to_fractional)

def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([]) == []
    assert get_longest_equal_int_real([52.52, 41.41, 21.21, 14.2, 54.54, 13.3]) == [52.52,41.41,21.21]
    assert get_longest_equal_int_real([1.1, 5.5, 23.2, 51.2, 16.0]) == [1.1, 5.5]
    assert get_longest_equal_int_real([28.3, 51.9, 63.4]) == []

test_get_longest_equal_int_real()
