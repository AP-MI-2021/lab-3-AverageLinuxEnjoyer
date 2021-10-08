from get_longest_subsequence import get_longest_subsequence

def are_concat_digits_asc(lst: list[int]) -> bool:
    """Verifica daca concatenarea numerelor unei liste are cifrele in ordine crescatoare

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca are loc conditia, False in caz contrar
    """
    concat = "".join([str(x) for x in lst])
    
    for i in range(1, len(concat)):
        if concat[i] <= concat[i-1]:
            return False

    return True

def test_are_concat_digits_asc():
    assert are_concat_digits_asc([12,45,69]) == True
    assert are_concat_digits_asc([]) == True
    assert are_concat_digits_asc([421,63]) == False
    assert are_concat_digits_asc([12]) == True

test_are_concat_digits_asc()

def get_longest_concat_digits_asc(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa de numere a caror concatenare are cifrele in ordine crescatoare

    Args:
        lst (list[int]): Lista principala, din care e verificata fiecare subsecventa

    Returns:
        list[int]: Subsecventa ce respecta proprietatea
    """
    return get_longest_subsequence(lst, are_concat_digits_asc)

def test_get_longest_concat_digits_asc():
    assert get_longest_concat_digits_asc([258, 9, 63, 28]) == [258, 9]
    assert get_longest_concat_digits_asc([73, 85, 83]) == []
    assert get_longest_concat_digits_asc([]) == []
    assert get_longest_concat_digits_asc([621, 456, 89, 1, 23, 67, 5]) == [1,23,67]

test_get_longest_concat_digits_asc()