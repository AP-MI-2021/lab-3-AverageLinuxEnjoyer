from get_longest_subsequence import get_longest_subsequence

def is_palindrome(x: int) -> bool:
    """Verifica daca un numar e palindrom

    Args:
        x (int): Numarul verificat

    Returns:
        bool: True daca e palindrom, False in caz contrar
    """
    return str(x) == str(x)[::-1]

def test_is_palindrome():
    assert is_palindrome(5) == True
    assert is_palindrome(101) == True
    assert is_palindrome(1234) == False
    assert is_palindrome(92816541237) == False

test_is_palindrome()


def are_all_palindromes(lst: list[int]) -> bool:
    """Verifica daca toate numerele dintr-o lista sunt palindroame

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca toate numerele din lista sunt palindroame, False in caz contrar
    """
    for x in lst:
        if not is_palindrome(x):
            return False

    return True


def test_are_all_palindromes():
    assert are_all_palindromes([101,23432, 515]) == True
    assert are_all_palindromes([54,23,818]) == False
    assert are_all_palindromes([]) == True
    assert are_all_palindromes([1,0,9,2]) == True

test_are_all_palindromes()

def get_longest_all_palindromes(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa de numere care sunt palindroame dintr-o lista

    Args:
        lst (list[int]): Lista cu toate elementele

    Returns:
        list[int]: Subsecventa cu palindroame
    """
    return get_longest_subsequence(lst, are_all_palindromes)

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([54,21,636,666,21812, 53,14]) == [636,666,21812]
    assert get_longest_all_palindromes([0,1,2,3,4]) == [0,1,2,3,4]
    assert get_longest_all_palindromes([14]) == []
    assert get_longest_all_palindromes([2]) == [2]

test_get_longest_all_palindromes()