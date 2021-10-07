from get_longest_subsequence import get_longest_subsequence

def are_sorted(lst: list[int]) -> bool:
    """Verifica daca o lista este sortata crescator

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca este sortata, False in caz contrar
    """
    for i in range(1,len(lst)):
        if lst[i-1] > lst[i]:
            return False

    return True

def test_are_sorted():
    assert are_sorted([]) == True
    assert are_sorted([1,2,2,5,20]) == True
    assert are_sorted([4,6,7,2,5,9,10]) == False
    assert are_sorted([-1,5,2]) == False

test_are_sorted() 

def get_longest_sorted_asc(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa cu numere ordonate crescator dintr-o lista

    Args:
        lst (list[int]): Subsecventa cu numere ordonate crescator
    
    Returns:
        list[int]: Lista cu toate numerele
    """
    return get_longest_subsequence(lst, are_sorted)

def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1,2,7,4,1,2,4,8,20,23]) ==  [1,2,4,8,20,23]
    assert get_longest_sorted_asc([]) == []
    assert get_longest_sorted_asc([-3]) == [-3]
    assert get_longest_sorted_asc([7,3,2,1]) == [7]

test_get_longest_sorted_asc()