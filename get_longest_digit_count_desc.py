from get_longest_subsequence import get_longest_subsequence

def are_digit_count_desc(lst: list[int]) -> bool:
    """Verifica daca numarul de cifre ale elementelor unei liste sunt in ordine descrescatoare

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca sunt in ordine descrescatoare, False in caz contrar
    """
    for i in range(1, len(lst)):
        if len(str(lst[i])) >= len(str(lst[i-1])):
            return False

    return True

def test_are_digit_count_desc():
    assert are_digit_count_desc([29,3]) == True
    assert are_digit_count_desc([]) == True
    assert are_digit_count_desc([14]) == True
    assert are_digit_count_desc([41,29,365]) == False

test_are_digit_count_desc()

def get_longest_digit_count_desc(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa in care elementele au numarul de cifre in ordine descrescatoare

    Args:
        lst (list[int]): Lista principala

    Returns:
        list[int]: Subsecventa returnata
    """
    return get_longest_subsequence(lst, are_digit_count_desc)

def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([21,4,53, 82, 16]) == [21,4]
    assert get_longest_digit_count_desc([]) == []
    assert get_longest_digit_count_desc([53, 29, 41, 85]) == [53]
    assert get_longest_digit_count_desc([16, 163, 1634, 521]) == [1634, 521]

test_get_longest_digit_count_desc()