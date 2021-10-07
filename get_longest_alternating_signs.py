from get_longest_subsequence import get_longest_subsequence


def are_alternating_signs(lst: list[int]) -> bool:
    """Verifica daca toate elementele unei liste au semne alternante

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca elementele listei au semne alternante, False in caz contrar
    """
    if len(lst) > 0:
        plus_before = not (lst[0] >= 0)

    for x in lst:
        plus = (x >= 0)

        if plus == plus_before:
            return False

        plus_before = plus

    return True


def test_are_alternating_signs():
    assert are_alternating_signs([-1, 1, -2, 5, -21]) == True
    assert are_alternating_signs([]) == True
    assert are_alternating_signs([3, 4, -1, 2, -1, 6]) == False
    assert are_alternating_signs([5]) == True


test_are_alternating_signs()


def get_longest_alternating_signs(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa a unei liste in care numerele au semne alternante

    Args:
        lst (list[int]): Lista cu toate numerele

    Returns:
        list[int]: Cea mai lunga subsecventa cu semne alternante
    """
    return get_longest_subsequence(lst, are_alternating_signs)


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([-1, 4, 7, -2, -7, 1, 17, -1, 8, -9]) == [17, -1, 8, -9]
    assert get_longest_alternating_signs([]) == []
    assert get_longest_alternating_signs([5]) == [5]
    assert get_longest_alternating_signs([47, -52, -31, -47, 21, -3, 1, -5]) == [-47, 21, -3, 1, -5]


test_get_longest_alternating_signs()
